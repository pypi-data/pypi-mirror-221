use std::borrow::Borrow;
use std::collections::HashMap;
use std::rc::Rc;

use klvm_rs::allocator;
use klvm_rs::allocator::{Allocator, NodePtr};

use num_bigint::ToBigInt;

use sha2::Digest;
use sha2::Sha256;

use crate::classic::klvm::__type_compatibility__::{bi_one, bi_zero};
use crate::classic::klvm_tools::stages::stage_0::TRunProgram;

use crate::compiler::prims;
use crate::compiler::runtypes::RunFailure;
use crate::compiler::sexp::{parse_sexp, SExp};
use crate::compiler::srcloc::Srcloc;

use crate::util::{number_from_u8, u8_from_number, Number};

/// An object which contains the state of a running KLVM program in a compact
/// form.
///
/// Being immutable, it can be preserved, examined and compared as desired.  The
/// whole record of KLVM execution can be observed by collecting these until the
/// program is in the Done state.
#[derive(Clone, Debug)]
pub enum RunStep {
    /// The state of a program (or subprogram) that completed.
    /// Contains a location taken from the operator that completed and the result
    /// value.
    Done(Srcloc, Rc<SExp>),
    /// An operator producing a result.  The operator has run and the result is
    /// given.  The final argument is a refcounted pointer to a step that the
    /// operator's result will be returned to if it stepped again.
    OpResult(Srcloc, Rc<SExp>, Rc<RunStep>),
    /// An operator in flight.  The arguments are
    /// - An operator
    /// - The environment
    /// - The tail of the expression if an operator, in progress.
    /// - When present, a list of arguments remaining to evaluate, otherwise
    ///   the expression is ready to run the operator on.
    /// - The RunStep to which this step returns a value when complete.
    Op(
        Rc<SExp>,
        Rc<SExp>,
        Rc<SExp>,
        Option<Vec<Rc<SExp>>>,
        Rc<RunStep>,
    ),
    /// A step about to be taken.  Indicates a klvm expression and env, plus the
    /// parent to which its value is returned.
    Step(Rc<SExp>, Rc<SExp>, Rc<RunStep>),
}

impl RunStep {
    pub fn parent(&self) -> Option<Rc<RunStep>> {
        match self {
            RunStep::Done(_, _) => None,
            RunStep::OpResult(_, _, p) => Some(p.clone()),
            RunStep::Op(_, _, _, _, p) => Some(p.clone()),
            RunStep::Step(_, _, p) => Some(p.clone()),
        }
    }

    pub fn sexp(&self) -> Rc<SExp> {
        match self {
            RunStep::Done(_, s) => s.clone(),
            RunStep::OpResult(_, s, _) => s.clone(),
            RunStep::Op(e, _, _, _, _) => e.clone(),
            RunStep::Step(e, _, _) => e.clone(),
        }
    }

    pub fn args(&self) -> Option<Rc<SExp>> {
        match self {
            RunStep::Step(_, a, _) => Some(a.clone()),
            RunStep::Op(_, a, _, _, _) => Some(a.clone()),
            _ => None,
        }
    }

    pub fn loc(&self) -> Srcloc {
        match self {
            RunStep::Done(l, _) => l.clone(),
            RunStep::OpResult(l, _, _) => l.clone(),
            RunStep::Op(e, _, _, _, _) => e.loc(),
            RunStep::Step(e, _, _) => e.loc(),
        }
    }
}

fn choose_path(
    l: Srcloc,
    orig: Number,
    p: Number,
    all: Rc<SExp>,
    context: Rc<SExp>,
) -> Result<Rc<SExp>, RunFailure> {
    if p == bi_one() {
        Ok(context)
    } else {
        match context.borrow() {
            SExp::Cons(l, a, b) => {
                let next = if p.clone() % 2_i32.to_bigint().unwrap() == bi_zero() {
                    a
                } else {
                    b
                };

                choose_path(
                    l.clone(),
                    orig,
                    p / (2_i32.to_bigint().unwrap()),
                    all,
                    next.clone(),
                )
            }

            _ => Err(RunFailure::RunErr(l, format!("bad path {orig} in {all}"))),
        }
    }
}

fn translate_head(
    allocator: &mut Allocator,
    runner: Rc<dyn TRunProgram>,
    prim_map: Rc<HashMap<Vec<u8>, Rc<SExp>>>,
    _l: Srcloc,
    sexp: Rc<SExp>,
    context: Rc<SExp>,
) -> Result<Rc<SExp>, RunFailure> {
    match sexp.borrow() {
        SExp::Nil(l) => Err(RunFailure::RunErr(
            l.clone(),
            "cannot apply nil".to_string(),
        )),
        SExp::QuotedString(l, _, v) => translate_head(
            allocator,
            runner,
            prim_map,
            l.clone(),
            Rc::new(SExp::Atom(l.clone(), v.clone())),
            context,
        ),
        SExp::Atom(l, v) => match prim_map.get(v) {
            None => translate_head(
                allocator,
                runner,
                prim_map,
                l.clone(),
                Rc::new(SExp::Integer(l.clone(), number_from_u8(v))),
                context,
            ),
            Some(v) => Ok(Rc::new(v.with_loc(l.clone()))),
        },
        SExp::Integer(l, i) => match prim_map.get(&u8_from_number(i.clone())) {
            None => Ok(sexp.clone()),
            Some(v) => Ok(Rc::new(v.with_loc(l.clone()))),
        },
        SExp::Cons(_l, _a, nil) => match nil.borrow() {
            SExp::Nil(_l1) => run(allocator, runner, prim_map, sexp.clone(), context, None),
            _ => Err(RunFailure::RunErr(
                sexp.loc(),
                format!("Unexpected head form in klvm {sexp}"),
            )),
        },
    }
}

fn eval_args(
    _allocator: &mut Allocator,
    _runner: Rc<dyn TRunProgram>,
    _prim_map: Rc<HashMap<Vec<u8>, Rc<SExp>>>,
    head: Rc<SExp>,
    sexp_: Rc<SExp>,
    context_: Rc<SExp>,
    parent: Rc<RunStep>,
) -> Result<RunStep, RunFailure> {
    let mut sexp = sexp_.clone();
    let mut eval_list: Vec<Rc<SExp>> = Vec::new();

    loop {
        match sexp.borrow() {
            SExp::Nil(_l) => {
                return Ok(RunStep::Op(head, context_, sexp, Some(eval_list), parent));
            }
            SExp::Cons(_l, a, b) => {
                eval_list.push(a.clone());
                sexp = b.clone();
            }
            _ => {
                return Err(RunFailure::RunErr(
                    sexp.loc(),
                    format!("bad argument list {sexp_} {context_}"),
                ));
            }
        }
    }
}

/// Given an SExp, produce a klvmr style NodePtr in the given allocator.
pub fn convert_to_klvm_rs(
    allocator: &mut Allocator,
    head: Rc<SExp>,
) -> Result<NodePtr, RunFailure> {
    match head.borrow() {
        SExp::Nil(_) => Ok(allocator.null()),
        SExp::Atom(_l, x) => allocator
            .new_atom(x)
            .map_err(|_e| RunFailure::RunErr(head.loc(), format!("failed to alloc atom {head}"))),
        SExp::QuotedString(_, _, x) => allocator
            .new_atom(x)
            .map_err(|_e| RunFailure::RunErr(head.loc(), format!("failed to alloc string {head}"))),
        SExp::Integer(_, i) => {
            if *i == bi_zero() {
                Ok(allocator.null())
            } else {
                allocator
                    .new_atom(&u8_from_number(i.clone()))
                    .map_err(|_e| {
                        RunFailure::RunErr(head.loc(), format!("failed to alloc integer {head}"))
                    })
            }
        }
        SExp::Cons(_, a, b) => convert_to_klvm_rs(allocator, a.clone()).and_then(|head| {
            convert_to_klvm_rs(allocator, b.clone()).and_then(|tail| {
                allocator.new_pair(head, tail).map_err(|_e| {
                    RunFailure::RunErr(a.loc(), format!("failed to alloc cons {head}"))
                })
            })
        }),
    }
}

/// Given an allocator and klvmr NodePtr, produce an SExp which is equivalent.
pub fn convert_from_klvm_rs(
    allocator: &mut Allocator,
    loc: Srcloc,
    head: NodePtr,
) -> Result<Rc<SExp>, RunFailure> {
    match allocator.sexp(head) {
        allocator::SExp::Atom(h) => {
            if h.is_empty() {
                Ok(Rc::new(SExp::Nil(loc)))
            } else {
                let atom_data = allocator.buf(&h);
                let integer = number_from_u8(atom_data);
                // Ensure that atom values that don't evaluate equal to integers
                // are represented faithfully as atoms.
                if u8_from_number(integer.clone()) == atom_data {
                    Ok(Rc::new(SExp::Integer(loc, integer)))
                } else {
                    Ok(Rc::new(SExp::Atom(loc, atom_data.to_vec())))
                }
            }
        }
        allocator::SExp::Pair(a, b) => {
            convert_from_klvm_rs(allocator, loc.clone(), a).and_then(|h| {
                convert_from_klvm_rs(allocator, loc.clone(), b)
                    .map(|t| Rc::new(SExp::Cons(loc.clone(), h, t)))
            })
        }
    }
}

fn generate_argument_refs(start: Number, sexp: Rc<SExp>) -> Rc<SExp> {
    match sexp.borrow() {
        SExp::Cons(l, a, b) => {
            let next_index = bi_one() + 2_i32.to_bigint().unwrap() * start.clone();
            let tail = generate_argument_refs(next_index, b.clone());
            Rc::new(SExp::Cons(
                l.clone(),
                Rc::new(SExp::Integer(a.loc(), start)),
                tail,
            ))
        }
        _ => sexp.clone(),
    }
}

fn apply_op(
    allocator: &mut Allocator,
    runner: Rc<dyn TRunProgram>,
    l: Srcloc,
    head: Rc<SExp>,
    args: Rc<SExp>,
) -> Result<Rc<SExp>, RunFailure> {
    let wrapped_args = Rc::new(SExp::Cons(
        l.clone(),
        Rc::new(SExp::Nil(l.clone())),
        args.clone(),
    ));
    let application = Rc::new(SExp::Cons(
        l,
        head.clone(),
        generate_argument_refs(5_i32.to_bigint().unwrap(), args),
    ));
    let converted_app = convert_to_klvm_rs(allocator, application.clone())?;
    let converted_args = convert_to_klvm_rs(allocator, wrapped_args.clone())?;

    runner
        .run_program(allocator, converted_app, converted_args, None)
        .map_err(|e| {
            RunFailure::RunErr(
                head.loc(),
                format!("{} in {application} {wrapped_args}", e.1),
            )
        })
        .and_then(|v| convert_from_klvm_rs(allocator, head.loc(), v.1))
}

fn atom_value(head: Rc<SExp>) -> Result<Number, RunFailure> {
    match head.borrow() {
        SExp::Integer(_, i) => Ok(i.clone()),
        SExp::Nil(_) => Ok(bi_zero()),
        SExp::QuotedString(_, _, s) => Ok(number_from_u8(s)),
        SExp::Atom(_, s) => Ok(number_from_u8(s)),
        SExp::Cons(l, _, _) => Err(RunFailure::RunErr(
            l.clone(),
            format!("cons is not a number {head}"),
        )),
    }
}

/// Tell how many parents are in the parent step chain until completion.
pub fn get_history_len(step: Rc<RunStep>) -> usize {
    match step.borrow() {
        RunStep::Done(_, _) => 1,
        RunStep::OpResult(_, _, p) => 1 + get_history_len(p.clone()),
        RunStep::Op(_, _, _, _, p) => 1 + get_history_len(p.clone()),
        RunStep::Step(_, _, p) => 1 + get_history_len(p.clone()),
    }
}

/// Generically determine whether a value is truthy.
pub fn truthy(sexp: Rc<SExp>) -> bool {
    // Fails for cons, but cons is truthy
    atom_value(sexp).unwrap_or_else(|_| bi_one()) != bi_zero()
}

/// The second of the core run operations, combine determines how a recently
/// completed step affects its parent to produce the next evaluation step.
///
/// For example, when a finished operation is combined with a parent that needs
/// more arguments for its operator, one needed argument evaluation is removed
/// and the step becomes closer to evaluation.
pub fn combine(a: &RunStep, b: &RunStep) -> RunStep {
    match (a, b.borrow()) {
        (RunStep::Done(l, x), RunStep::Done(_, _)) => RunStep::Done(l.clone(), x.clone()),
        (RunStep::Done(l, x), RunStep::Op(head, context, args, Some(remain), parent)) => {
            RunStep::Op(
                head.clone(),
                context.clone(),
                Rc::new(SExp::Cons(l.clone(), x.clone(), args.clone())),
                Some(remain.clone()),
                parent.clone(),
            )
        }
        (RunStep::Done(_l, _x), RunStep::Op(_head, _context, _args, None, parent)) => {
            combine(a, parent.borrow())
        }
        (RunStep::Done(_l, _x), RunStep::Step(_sexp, _context, parent)) => {
            combine(a, parent.borrow())
        }
        _ => a.clone(),
    }
}

pub fn flatten_signed_int(v: Number) -> Number {
    let mut sign_digits = v.to_signed_bytes_le();
    sign_digits.push(0);
    Number::from_signed_bytes_le(&sign_digits)
}

/// Given a RunStep, return a RunStep whose top operation returns <value>
pub fn step_return_value(step: &RunStep, value: Rc<SExp>) -> RunStep {
    step.parent()
        .map(|p| RunStep::OpResult(value.loc(), value.clone(), p))
        .unwrap_or_else(|| RunStep::Done(value.loc(), value.clone()))
}

/// The main operation to step the machine.  Given a RunStep, produce a new RunStep
/// which is one step farther toward a result.  When complete, the result is a
/// Done value.
pub fn run_step(
    allocator: &mut Allocator,
    runner: Rc<dyn TRunProgram>,
    prim_map: Rc<HashMap<Vec<u8>, Rc<SExp>>>,
    step_: &RunStep,
) -> Result<RunStep, RunFailure> {
    let mut step = step_.clone();

    match &step {
        RunStep::OpResult(l, x, p) => {
            let parent: &RunStep = p.borrow();
            return Ok(combine(&RunStep::Done(l.clone(), x.clone()), parent));
        }
        RunStep::Done(_l, _x) => {}
        RunStep::Step(sexp, context, parent) => {
            match sexp.borrow() {
                SExp::Integer(l, v) => {
                    /* An integer picks a value from the context */
                    let flat_v = flatten_signed_int(v.clone());
                    return Ok(RunStep::OpResult(
                        l.clone(),
                        choose_path(
                            l.clone(),
                            flat_v.clone(),
                            flat_v,
                            context.clone(),
                            context.clone(),
                        )?,
                        Rc::new(step_.clone()),
                    ));
                }
                SExp::QuotedString(l, _, v) => {
                    step = RunStep::Step(
                        Rc::new(SExp::Integer(l.clone(), number_from_u8(v))),
                        context.clone(),
                        parent.clone(),
                    );
                }
                SExp::Atom(l, v) => {
                    step = RunStep::Step(
                        Rc::new(SExp::Integer(l.clone(), number_from_u8(v))),
                        context.clone(),
                        parent.clone(),
                    );
                }
                SExp::Nil(l) => {
                    return Ok(RunStep::OpResult(
                        l.clone(),
                        sexp.clone(),
                        Rc::new(step_.clone()),
                    ));
                }
                SExp::Cons(l, a, b) => {
                    let head = Rc::new(
                        translate_head(
                            allocator,
                            runner.clone(),
                            prim_map.clone(),
                            l.clone(),
                            a.clone(),
                            context.clone(),
                        )?
                        .with_loc(l.clone()),
                    );

                    if atom_value(head.clone())? == bi_one() {
                        step = RunStep::Done(l.clone(), b.clone());
                    } else {
                        step = eval_args(
                            allocator,
                            runner.clone(),
                            prim_map,
                            head,
                            b.clone(),
                            context.clone(),
                            parent.clone(),
                        )?;
                    }
                }
            }
        }
        RunStep::Op(head, context, tail, Some(rest), parent) => {
            let mut rest_mut = rest.clone();
            match rest_mut.pop() {
                Some(x) => {
                    step = RunStep::Step(
                        x,
                        context.clone(),
                        Rc::new(RunStep::Op(
                            head.clone(),
                            context.clone(),
                            tail.clone(),
                            Some(rest_mut),
                            parent.clone(),
                        )),
                    );
                }
                None => {
                    step = RunStep::Op(
                        head.clone(),
                        context.clone(),
                        tail.clone(),
                        None,
                        parent.clone(),
                    );
                }
            }
        }
        RunStep::Op(head, _context, tail, None, parent) => {
            let aval = atom_value(head.clone())?;
            let apply_atom = 2_i32.to_bigint().unwrap();
            let if_atom = 3_i32.to_bigint().unwrap();
            let cons_atom = 4_i32.to_bigint().unwrap();
            let first_atom = 5_i32.to_bigint().unwrap();
            let rest_atom = 6_i32.to_bigint().unwrap();

            let wanted_args: i32 = if aval == if_atom {
                3
            } else if aval == cons_atom || aval == apply_atom {
                2
            } else if aval == first_atom || aval == rest_atom {
                1
            } else {
                -1
            };

            let op = if aval == apply_atom {
                "apply".to_string()
            } else if aval == if_atom {
                "i (primitive if)".to_string()
            } else if aval == cons_atom {
                "cons".to_string()
            } else if aval == first_atom {
                "first".to_string()
            } else if aval == rest_atom {
                "rest".to_string()
            } else {
                format!("operator {aval}")
            };

            match tail.proper_list() {
                None => {
                    return Err(RunFailure::RunErr(
                        tail.loc(),
                        format!("Bad arguments given to cons {tail}"),
                    ));
                }
                Some(l) => {
                    if wanted_args != -1 && l.len() as i32 != wanted_args {
                        return Err(RunFailure::RunErr(
                            tail.loc(),
                            format!("Wrong number of parameters to {op}: {tail}"),
                        ));
                    }

                    if aval == if_atom {
                        let outcome = if truthy(Rc::new(l[0].clone())) {
                            l[1].clone()
                        } else {
                            l[2].clone()
                        };

                        step = RunStep::Done(outcome.loc(), Rc::new(outcome));
                    } else if aval == cons_atom {
                        return Ok(RunStep::OpResult(
                            head.loc(),
                            Rc::new(SExp::Cons(
                                head.loc(),
                                Rc::new(l[0].clone()),
                                Rc::new(l[1].clone()),
                            )),
                            Rc::new(step_.clone()),
                        ));
                    } else if aval == first_atom || aval == rest_atom {
                        match &l[0] {
                            SExp::Cons(_, a, b) => {
                                if aval == first_atom {
                                    return Ok(RunStep::OpResult(
                                        a.loc(),
                                        a.clone(),
                                        Rc::new(step_.clone()),
                                    ));
                                } else {
                                    return Ok(RunStep::OpResult(
                                        b.loc(),
                                        b.clone(),
                                        Rc::new(step_.clone()),
                                    ));
                                }
                            }
                            _ => {
                                return Err(RunFailure::RunErr(
                                    tail.loc(),
                                    format!("Cons expected for {op}, got {tail}"),
                                ));
                            }
                        }
                    } else if aval == apply_atom {
                        step = RunStep::Step(
                            Rc::new(l[0].clone()),
                            Rc::new(l[1].clone()),
                            parent.clone(),
                        );
                    } else {
                        let result = apply_op(
                            allocator,
                            runner.clone(),
                            head.loc(),
                            head.clone(),
                            tail.clone(),
                        )?;

                        return Ok(RunStep::OpResult(
                            head.loc(),
                            result,
                            Rc::new(step_.clone()),
                        ));
                    }
                }
            }
        }
    }

    Ok(combine(&step, step_))
}

pub fn start_step(sexp_: Rc<SExp>, context_: Rc<SExp>) -> RunStep {
    RunStep::Step(
        sexp_.clone(),
        context_,
        Rc::new(RunStep::Done(sexp_.loc(), sexp_.clone())),
    )
}

/// Use the RunStep object to evaluate some klvm to completion.
pub fn run(
    allocator: &mut Allocator,
    runner: Rc<dyn TRunProgram>,
    prim_map: Rc<HashMap<Vec<u8>, Rc<SExp>>>,
    sexp_: Rc<SExp>,
    context_: Rc<SExp>,
    iter_limit: Option<usize>,
) -> Result<Rc<SExp>, RunFailure> {
    let mut step = start_step(sexp_, context_);
    let mut iters = 0;

    loop {
        if let Some(limit) = &iter_limit {
            if *limit <= iters {
                return Err(RunFailure::RunErr(step.sexp().loc(), "timeout".to_string()));
            }
        }
        iters += 1;
        step = run_step(allocator, runner.clone(), prim_map.clone(), &step)?;
        if let RunStep::Done(_, x) = step {
            return Ok(x);
        }
    }
}

/// A convenience function which, givne a text program, its arguments and filename,
/// parses the klvm text and runs to completion.
pub fn parse_and_run(
    allocator: &mut Allocator,
    runner: Rc<dyn TRunProgram>,
    file: &str,
    content: &str,
    args: &str,
    step_limit: Option<usize>,
) -> Result<Rc<SExp>, RunFailure> {
    let code = parse_sexp(Srcloc::start(file), content.bytes())
        .map_err(|e| RunFailure::RunErr(e.0, e.1))?;
    let args =
        parse_sexp(Srcloc::start(file), args.bytes()).map_err(|e| RunFailure::RunErr(e.0, e.1))?;

    if code.is_empty() {
        Err(RunFailure::RunErr(
            Srcloc::start(file),
            "no code".to_string(),
        ))
    } else if args.is_empty() {
        Err(RunFailure::RunErr(
            Srcloc::start(file),
            "no args".to_string(),
        ))
    } else {
        let prim_map = prims::prim_map();
        run(
            allocator,
            runner,
            prim_map,
            code[0].clone(),
            args[0].clone(),
            step_limit,
        )
    }
}

pub fn sha256tree_from_atom(v: &[u8]) -> Vec<u8> {
    let mut hasher = Sha256::new();
    hasher.update([1]);
    hasher.update(v);
    hasher.finalize().to_vec()
}

/// sha256tree for modern style SExp
pub fn sha256tree(s: Rc<SExp>) -> Vec<u8> {
    match s.borrow() {
        SExp::Cons(_l, a, b) => {
            let mut hasher = Sha256::new();
            let t1 = sha256tree(a.clone());
            let t2 = sha256tree(b.clone());
            hasher.update([2]);
            hasher.update(&t1);
            hasher.update(&t2);
            hasher.finalize().to_vec()
        }
        SExp::Nil(_) => sha256tree_from_atom(&[]),
        SExp::Integer(_, i) => sha256tree_from_atom(&u8_from_number(i.clone())),
        SExp::QuotedString(_, _, v) => sha256tree_from_atom(v),
        SExp::Atom(_, v) => sha256tree_from_atom(v),
    }
}
