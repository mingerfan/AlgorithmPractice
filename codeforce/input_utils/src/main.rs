macro_rules! input {
    ($buf:expr, $($r:tt)*) => {
        input_inner!{$buf, $($r)*}
    };
}

macro_rules! input_inner {
    ($buf:expr) => {};
    ($buf:expr, ) => {};
    ($buf:expr, $var:tt : $t:tt($func:expr) $($r:tt)*) => {
        let $var = $func(read_value!($buf, $t));
        input_inner!{$buf $($r)*}
    };
    ($buf:expr, $var:tt : [$t:ty] $($r:tt)*) => {
        let $var = read_value!($buf, [$t]);
        input_inner!{$buf $($r)*}
    };
    ($buf: expr, $var:tt : $t:tt $($r:tt)*) => {
        let $var = read_value!($buf, $t);
        input_inner!{$buf $($r)*}
    };
}

macro_rules! get {
    ($buf: expr) => {{
        std::io::stdin().read_line(&mut $buf).unwrap();
        let new = $buf.trim().to_string();
        $buf.clear();
        new
    }};
    ($buf: expr, [$t:ty]) => {{
        std::io::stdin().read_line(&mut $buf).unwrap();
        let new = $buf.split_whitespace()
            .map(|x| x.parse::<$t>().unwrap())
            .collect::<Vec<$t>>();
        $buf.clear();
        new
    }};
    ($buf: expr, $t: ty) => {{
        std::io::stdin().read_line(&mut $buf).unwrap();
        let new = $buf.trim().parse::<$t>().unwrap();
        $buf.clear();
        new
    }};
}

macro_rules! read_value {
    ($buf: expr, usize) => {
        get!($buf, usize)
    };
    ($buf: expr, i32) => {
        get!($buf, i32)
    };
    ($buf: expr, i64) => {
        get!($buf, i64)
    };
    ($buf: expr, [$t:ty]) => {
        get!($buf, [$t])
    };
    ($buf: expr, String) => {
        get!($buf)
    };
    ($buf: expr, $t:ty) => {
        get!($buf, $t)
    };
}

fn main() {
    let mut buf = String::new();
    input! {
        buf,
        numbers: String (|s: String| -> Vec<usize> {
            s.split_whitespace()
             .map(|x| x.parse::<usize>().unwrap())
             .collect()
        }),
    }

    input! {
        buf,
        n: usize,
        t: u128,
        test1: [i32],
    }
    // let sum: i32 = numbers.iter().sum();
    // println!("{}", sum);
    println!("{numbers:?}");
    println!("{n} {t} {test1:?}");
}
