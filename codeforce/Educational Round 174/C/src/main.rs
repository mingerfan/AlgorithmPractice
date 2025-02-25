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
        let new = $buf
            .split_whitespace()
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

fn add(a: u64, b: u64) -> u64 {
    (a + b) % 998244353
}

fn main() {
    let mut buf = String::new();
    input! {
        buf,
        t: usize,
    }
    for _ in 0..t {
        input! {
            buf,
            _n: usize,
            a: [u64],
        }
        let mut dp = vec![0u64; 4];
        dp[0] = 1;
        for i in a {
            if i == 2 {
                dp[2] = add(dp[2], dp[2]);
            }
            dp[i as usize] = add(dp[i as usize], dp[i as usize - 1]);
        }
        println!("{}", dp[3]);
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_main() {
        let res = cf_test_utils::run_with_stdin_file("target/debug/C.exe", "input.txt");
        println!("{}", res.unwrap());
    }
}
