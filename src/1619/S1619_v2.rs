impl Solution {
    pub fn trim_mean(arr: Vec<i32>) -> f64 {
        let mut a = arr;
        a.sort_unstable();
        let r = a.len() / 20;
        let s:i32 = a[r..a.len()-r].iter().sum();
        s as f64 / (a.len() - r * 2) as f64
    }
}
