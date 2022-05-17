impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut res = 0;
        for char in s.chars().rev() {
            if &char != &' ' { res += 1; }
            if &char == &' ' && res != 0 { return res; }
        }
        res
    }
}
