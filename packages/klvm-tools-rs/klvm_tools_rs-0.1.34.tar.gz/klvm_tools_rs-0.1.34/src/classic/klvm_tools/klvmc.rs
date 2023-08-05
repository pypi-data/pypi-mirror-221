use std::collections::HashMap;
use std::fs;
use std::io::Write;
use std::path::Path;
use std::rc::Rc;

use tempfile::NamedTempFile;

use klvm_rs::allocator::{Allocator, NodePtr, SExp};
use klvm_rs::reduction::EvalErr;

use crate::classic::klvm::__type_compatibility__::Stream;
use crate::classic::klvm::serialize::sexp_to_stream;
use crate::classic::klvm::sexp::proper_list;
use crate::classic::klvm_tools::binutils::{assemble_from_ir, disassemble};
use crate::classic::klvm_tools::ir::reader::read_ir;
use crate::classic::klvm_tools::stages::run;
use crate::classic::klvm_tools::stages::stage_0::{DefaultProgramRunner, TRunProgram};
use crate::classic::klvm_tools::stages::stage_2::operators::run_program_for_search_paths;

use crate::classic::platform::distutils::dep_util::newer;

use crate::compiler::compiler::compile_file;
use crate::compiler::compiler::run_optimizer;
use crate::compiler::compiler::DefaultCompilerOpts;
use crate::compiler::comptypes::CompileErr;
use crate::compiler::comptypes::CompilerOpts;
use crate::compiler::klvm::convert_to_klvm_rs;
use crate::compiler::runtypes::RunFailure;

fn include_dialect(
    allocator: &mut Allocator,
    dialects: &HashMap<Vec<u8>, i32>,
    e: &[NodePtr],
) -> Option<i32> {
    if let (SExp::Atom(inc), SExp::Atom(name)) = (allocator.sexp(e[0]), allocator.sexp(e[1])) {
        if allocator.buf(&inc) == "include".as_bytes().to_vec() {
            if let Some(dialect) = dialects.get(allocator.buf(&name)) {
                return Some(*dialect);
            }
        }
    }

    None
}

pub fn write_sym_output(
    compiled_lookup: &HashMap<String, String>,
    path: &str,
) -> Result<(), String> {
    let output = serde_json::to_string(compiled_lookup)
        .map_err(|_| "failed to serialize to json".to_string())?;

    fs::write(path, output)
        .map_err(|_| format!("failed to write {path}"))
        .map(|_| ())
}

pub fn detect_modern(allocator: &mut Allocator, sexp: NodePtr) -> Option<i32> {
    let mut dialects = HashMap::new();
    dialects.insert("*standard-cl-21*".as_bytes().to_vec(), 21);
    dialects.insert("*standard-cl-22*".as_bytes().to_vec(), 22);

    proper_list(allocator, sexp, true).and_then(|l| {
        for elt in l.iter() {
            if let Some(dialect) = detect_modern(allocator, *elt) {
                return Some(dialect);
            }

            match proper_list(allocator, *elt, true) {
                None => {
                    continue;
                }

                Some(e) => {
                    if e.len() != 2 {
                        continue;
                    }

                    if let Some(dialect) = include_dialect(allocator, &dialects, &e) {
                        return Some(dialect);
                    }
                }
            }
        }

        None
    })
}

pub fn compile_klvm_text(
    allocator: &mut Allocator,
    opts: Rc<dyn CompilerOpts>,
    symbol_table: &mut HashMap<String, String>,
    text: &str,
    input_path: &str,
    classic_with_opts: bool,
) -> Result<NodePtr, EvalErr> {
    let ir_src = read_ir(text).map_err(|s| EvalErr(allocator.null(), s.to_string()))?;
    let assembled_sexp = assemble_from_ir(allocator, Rc::new(ir_src))?;

    if let Some(dialect) = detect_modern(allocator, assembled_sexp) {
        let runner = Rc::new(DefaultProgramRunner::new());
        let opts = opts.set_optimize(true).set_frontend_opt(dialect > 21);

        let unopt_res = compile_file(allocator, runner.clone(), opts, text, symbol_table);
        let res = unopt_res.and_then(|x| run_optimizer(allocator, runner, Rc::new(x)));

        res.and_then(|x| {
            convert_to_klvm_rs(allocator, x).map_err(|r| match r {
                RunFailure::RunErr(l, x) => CompileErr(l, x),
                RunFailure::RunExn(l, x) => CompileErr(l, x.to_string()),
            })
        })
        .map_err(|s| EvalErr(allocator.null(), s.1))
    } else {
        let compile_invoke_code = run(allocator);
        let input_sexp = allocator.new_pair(assembled_sexp, allocator.null())?;
        let run_program = run_program_for_search_paths(input_path, &opts.get_search_paths(), false);
        if classic_with_opts {
            run_program.set_compiler_opts(Some(opts));
        }
        let run_program_output =
            run_program.run_program(allocator, compile_invoke_code, input_sexp, None)?;
        Ok(run_program_output.1)
    }
}

pub fn compile_klvm_inner(
    allocator: &mut Allocator,
    opts: Rc<dyn CompilerOpts>,
    symbol_table: &mut HashMap<String, String>,
    filename: &str,
    text: &str,
    result_stream: &mut Stream,
    classic_with_opts: bool,
) -> Result<(), String> {
    let result = compile_klvm_text(
        allocator,
        opts,
        symbol_table,
        text,
        filename,
        classic_with_opts,
    )
    .map_err(|x| format!("error {} compiling {}", x.1, disassemble(allocator, x.0)))?;
    sexp_to_stream(allocator, result, result_stream);
    Ok(())
}

pub fn compile_klvm(
    input_path: &str,
    output_path: &str,
    search_paths: &[String],
    symbol_table: &mut HashMap<String, String>,
) -> Result<String, String> {
    let mut allocator = Allocator::new();

    let compile = newer(input_path, output_path).unwrap_or(true);
    let mut result_stream = Stream::new(None);

    if compile {
        let text = fs::read_to_string(input_path)
            .map_err(|x| format!("error reading {input_path}: {x:?}"))?;
        let opts = Rc::new(DefaultCompilerOpts::new(input_path)).set_search_paths(search_paths);

        compile_klvm_inner(
            &mut allocator,
            opts,
            symbol_table,
            input_path,
            &text,
            &mut result_stream,
            false,
        )?;

        let target_data = result_stream.get_value().hex();

        let write_file = |output_path: &str, target_data: &str| -> Result<(), String> {
            let output_path_obj = Path::new(output_path);
            let output_dir = output_path_obj
                .parent()
                .map(Ok)
                .unwrap_or_else(|| Err("could not get parent of output path"))?;

            // Make the contents appear atomically so that other test processes
            // won't mistake an empty file for intended output.
            let mut temp_output_file = NamedTempFile::new_in(output_dir).map_err(|e| {
                format!("error creating temporary compiler output for {input_path}: {e:?}")
            })?;

            let err_text = format!("failed to write to {:?}", temp_output_file.path());
            let translate_err = |_| err_text.clone();

            temp_output_file
                .write_all(target_data.as_bytes())
                .map_err(translate_err)?;

            temp_output_file.write_all(b"\n").map_err(translate_err)?;

            temp_output_file.persist(output_path).map_err(|e| {
                format!("error persisting temporary compiler output {output_path}: {e:?}")
            })?;

            Ok(())
        };

        // Try to detect whether we'd put the same output in the output file.
        // Don't proceed if true.
        if let Ok(prev_content) = fs::read_to_string(output_path) {
            let prev_trimmed = prev_content.trim();
            let trimmed = target_data.trim();
            if prev_trimmed == trimmed {
                // We should try to overwrite here, but not fail if it doesn't
                // work.  This will accomodate both the read only scenario and
                // the scenario where a target file is newer and people want the
                // date to be updated.
                write_file(output_path, &target_data).ok();

                // It's the same program, bail regardless.
                return Ok(output_path.to_string());
            }
        }

        write_file(output_path, &target_data)?;
    }

    Ok(output_path.to_string())
}

// export function find_files(path: str = ""){
//   const r: string[] = [];
//   for(const {dirpath, filenames} of os_walk(path)){
//     for(const filename of filenames){
//       if(filename.endsWith(".klvm")){
//         const full_path = path_join(dirpath, filename);
//         const target = `${full_path}.hex}`;
//         compile_klvm(full_path, target);
//         r.push(target);
//       }
//     }
//   }
//   return r;
// }
