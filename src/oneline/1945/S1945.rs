impl Solution {
    pub fn get_lucky(s: String, k: i32) -> i32 {
        (0..k-1).fold(s.bytes().map(|x|(x-96) as i32).map(|x|x/10+x%10).sum(), |x, _| x.to_string().bytes().map(|x|(x-48) as i32).sum())
    }
}
