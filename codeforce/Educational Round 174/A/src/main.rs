macro_rules! input {
    ($buf:expr, $($r:tt)*) => {
        input_inner!{$buf, $($r)*}
    };
}

macro_rules! input_inner {
    ($buf:expr) => {};
    ($buf:expr, ) => {};
    ($buf:expr, $var:ident : $t:tt($func:expr) $($r:tt)*) => {
        let $var = $func(read_value!($buf, $t));
        input_inner!{$buf $($r)*}
    };
    ($buf:expr, $var:ident : [$t:ty] $($r:tt)*) => {
        let $var = read_value!($buf, [$t]);
        input_inner!{$buf $($r)*}
    };
    ($buf: expr, $var:ident : $t:tt $($r:tt)*) => {
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
        n: usize,
    }
    for _ in 0..n {
        input! {
            buf,
            _arr_len: usize,
            arr: [i32],
        }
        let arr = arr;
        let mut left = 0;
        let mut is_yes = true;
        for (idx, num) in arr.iter().enumerate() {
            // 识别 101 pattern
            let right = if idx == arr.len() - 1 {
                0
            } else {
                arr[idx + 1]
            };
            if left == 1 && *num == 0 && right == 1 {
                is_yes = false;
                break;
            }
            left = *num;
        }
        if is_yes {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}
