use num_bigint::BigInt;
use unicode_segmentation::UnicodeSegmentation;

pub type Number = BigInt;

// Thanks: https://www.reddit.com/r/rust/comments/bkkpkz/pkgversion_access_your_crates_version_number_as/
pub fn version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

pub fn number_from_u8(v: &[u8]) -> Number {
    let len = v.len();
    if len == 0 {
        0.into()
    } else {
        Number::from_signed_bytes_be(v)
    }
}

pub fn u8_from_number(v: Number) -> Vec<u8> {
    v.to_signed_bytes_be()
}

pub fn index_of_match<F, T>(cb: F, haystack: &[T]) -> i32
where
    F: Fn(&T) -> bool,
{
    for (i, ch) in haystack.iter().enumerate() {
        if cb(ch) {
            return i as i32;
        }
    }
    -1
}

pub fn skip_leading(s: &str, dash: &str) -> String {
    return s.graphemes(true).skip_while(|ch| dash == *ch).collect();
}

pub fn collapse<A>(r: Result<A, A>) -> A {
    match r {
        Ok(a) => a,
        Err(e) => e,
    }
}

pub trait ErrInto<D> {
    fn err_into(self) -> D;
}

impl<SrcErr, DestErr, DestRes> ErrInto<Result<DestRes, DestErr>> for Result<DestRes, SrcErr>
where
    DestErr: From<SrcErr>,
{
    fn err_into(self) -> Result<DestRes, DestErr> {
        self.map_err(|e| e.into())
    }
}
