impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let mut s = word.clone();
        let mut res = 0;
        while sequence.contains(&s) {
            s = s + &word;
            res += 1;
        }
        res
    }
}
