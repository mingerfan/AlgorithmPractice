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
            (_n, k): [u64](|x: Vec<u64>| (x[0], x[1])),
            s: String,
            penalty: [u64],
        }
        let mut penalty_t = penalty.clone();
        penalty_t.push(0);
        penalty_t.sort();
        penalty_t.dedup();
        // println!("penalty: {penalty_t:?}");
        let mut left = 0;
        let mut right = penalty_t.len() - 1;
        let chars = s.chars().collect::<Vec<char>>();
        while left < right {
            let mid = (left + right) / 2;
            let cur_penalty = penalty_t[mid];
            let mut cnt = 0;
            let mut should_change = false;
            for (idx, &i) in penalty.iter().enumerate() {
                if i > cur_penalty && chars[idx] == 'B' && !should_change {
                    cnt += 1;
                    should_change = true;
                } else if i > cur_penalty && chars[idx] == 'R' {
                    should_change = false;
                }
            }
            // println!("left: {left}, right: {right}, penalty: {cur_penalty}, cnt: {cnt}");
            if cnt > k {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        println!("{}", penalty_t[left]);
    }
}

mod tests {
    #[test]
    fn test_main() {
        let res = cf_test_utils::run_with_stdin_file("target/debug/C.exe", "input.txt");
        println!("{}", res.unwrap());
    }
}