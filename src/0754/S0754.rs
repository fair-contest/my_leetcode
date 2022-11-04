impl Solution {
    pub fn reach_number(target: i32) -> i32 {
        let mut t = if target < 0 {-target} else {target};
        let n = (((t<<1) as f64).sqrt() + 0.5) as i32;
        let s = n * n + n >> 1;
        if (s - t) & 1 == 0 || s == t {n} else {n + 1 + (n&1)} 
    }
}
