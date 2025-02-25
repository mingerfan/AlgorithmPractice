use std::io;
use std::cmp::max;

const W: usize = 30;

fn solve() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let mut iter = line.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let q: usize = iter.next().unwrap().parse().unwrap();

    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let a: Vec<i32> = line
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let mut pre = vec![0; n];
    if n > 0 {
        pre[0] = a[0];
        for i in 1..n {
            pre[i] = pre[i-1] ^ a[i];
        }
    }


    let mut last: Vec<[i32; W]> = vec![[0; W]; n];
    for i in 0..n {
        for j in 0..W {
            last[i][j] = 0;
        }
        if i > 0 {
            last[i] = last[i - 1];
        }
        let msb_a = if a[i] == 0 { 0 } else { 31 - a[i].leading_zeros() as usize };
        last[i][msb_a] = i as i32;

        for j in (0..W - 1).rev() {
            last[i][j] = max(last[i][j], last[i][j + 1]);
        }
    }

    for _ in 0..q {
        let mut line = String::new();
        io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        let mut x: i32 = iter.next().unwrap().parse().unwrap();

        let mut idx: i32 = (n - 1) as i32;
        while idx >= 0 && x > 0 {
            let msb = if x == 0 { 0 } else { 31 - x.leading_zeros() as usize };
            let nxt = last[idx as usize][msb];
            x ^= pre[idx as usize] ^ pre[nxt as usize];
            idx = nxt;
            if nxt < 0 || (nxt >= 0 && (nxt as usize) < n && a[nxt as usize] > x) { // Corrected break condition to handle nxt < 0 and valid index check
                break;
            }
            if nxt >= 0 { // Added check for nxt being a valid index before accessing a[nxt as usize]
                x ^= a[nxt as usize];
                idx -= 1;
            } else {
                break; // Break if nxt is -1 equivalent
            }

        }

        print!("{} ", n as i32 - idx - 1);
    }
    println!();
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let mut iter = line.split_whitespace();
    let t: i32 = iter.next().unwrap().parse().unwrap();

    for _ in 0..t {
        solve();
    }
}
