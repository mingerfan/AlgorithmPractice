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
        n: usize,
    }
    for _ in 0..n {
        input! {
            buf,
            (r, c): [usize](|x: Vec<usize>| {
                (x[0], x[1])
            }),
        }
        let mut table = vec![];
        for _ in 0..r {
            input! {
                buf,
                row: [i32],
            }
            table.push(row);
        }
        let mut has_neighbour = vec![0; r * c];
        let mut has_color = vec![0; r * c];
        for m in 0..r {
            for n in 0..c {
                has_color[table[m][n] as usize - 1] = 1;
                if m + 1 < r && table[m + 1][n] == table[m][n] {
                    has_neighbour[table[m][n] as usize - 1] = 1;
                }
                if n + 1 < c && table[m][n + 1] == table[m][n] {
                    has_neighbour[table[m][n] as usize - 1] = 1;
                }
            }
        }
        let res: i32 = has_color.iter().sum::<i32>() + has_neighbour.iter().sum::<i32>()
            - has_neighbour.iter().max().unwrap_or(&0)
            - 1;
        println!("{}", res);
    }
}

#[cfg(test)]
mod tests {
    use cf_test_utils::*;
    #[test]
    fn test_main() {
        let res = run_with_stdin_file(
            r#"D:\KnowledgeLib\Algorithm practice\codeforce\Educational Round 174\B\target\debug\B.exe"#,
            "input.txt",
        );
        println!("{}", res.unwrap());
    }
}
