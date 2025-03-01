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

fn main() {
    let mut buf = String::new();
    input! {
        buf,
        t: usize,
    }
    for _ in 0..t {
        input! {
            buf,
            (_n, x, k): [i128](|x: Vec<i128>| (x[0] as u64, x[1] as i64, x[2] as u64)),
            s: String,
        }
        let mut first_reach0 = false;
        let mut first_reach0_time = 0;
        let mut sec_reach0 = false;
        let mut period = 0;
        let mut temp_x = x;
        for (idx, i) in s.chars().enumerate() {
            if i == 'L' {
                temp_x -= 1;
            } else {
                temp_x += 1;
            }
            if temp_x == 0 {
                first_reach0 = true;
                first_reach0_time = idx + 1;
                break;
            }
        }
        if first_reach0 {
            let mut temp = 0;
            for (idx, i) in s.chars().enumerate() {
                if i == 'L' {
                    temp -= 1;
                } else {
                    temp += 1;
                }
                if temp == 0 {
                    sec_reach0 = true;
                    period = idx + 1;
                    break;
                }
            }
        }
        if first_reach0 {
            let mut res = 1;
            let temp_k = k - first_reach0_time as u64;
            if sec_reach0 {
                res += temp_k / period as u64;
            }
            println!("{res}");
        } else {
            println!("0");
        }
    }
}

mod tests {
    #[test]
    fn test_main() {
        let res = cf_test_utils::run_with_stdin_file("target/debug/B.exe", "input.txt");
        println!("{}", res.unwrap());
    }
}