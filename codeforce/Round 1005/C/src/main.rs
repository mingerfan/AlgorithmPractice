use std::io;

fn  main() {
    let mut inp = String::new();
    io::stdin().read_line(&mut inp).unwrap();
    let n = inp.trim().parse::<i64>().unwrap();
    
    for _ in 0..n {
        inp.clear();
        io::stdin().read_line(&mut inp).unwrap();
        let _len = inp.trim().parse::<i64>().unwrap();
        inp.clear();
        io::stdin().read_line(&mut inp).unwrap();
        let arr: Vec<i64> = inp
            .split_whitespace()
            .map(|x| x.parse::<i64>().unwrap())
            .collect();

        let mut neg_sum = arr.iter().filter(|&x| *x < 0).map(|&x| x * -1).sum::<i64>();
        let mut pos_sum = 0;
        let mut max_sum = neg_sum;
        // 枚举分界点
        for i in arr {
            if i < 0 {
                neg_sum -= i * -1;
            } else {
                pos_sum += i;
            }
            max_sum = if neg_sum + pos_sum < max_sum {
                max_sum
            } else {
                neg_sum + pos_sum
            };
        }
        println!("{}", max_sum);
    }
}
