// v2的写法内存消耗低于v1版本

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let n: i32 = s.as_bytes().into_iter().map(|&x| (x - 96) as i32).sum();
        let mut prev = 0;
        (1..&s.len() / 2 + 1).any(|i| -> bool {
            prev += (&s.as_bytes()[i] - 96) as i32;
            if &s.len() % i == 0 && &n % &prev == 0 {
                let mut x = i.clone();
                while &x != &s.len() {
                    if &s[0..i] != &s[x..x + &i] { break; }
                    x += &i;
                }
                if x == s.len() { return true; }
            }
            false
        })
    }
}
