impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        word[0..1].chars().all(|x|x.is_ascii_uppercase()) && word[1..].chars().all(|x|x.is_ascii_lowercase()) || word.chars().all(|x|x.is_ascii_uppercase()) || word.chars().all(|x|x.is_ascii_lowercase()) 
    }
}
