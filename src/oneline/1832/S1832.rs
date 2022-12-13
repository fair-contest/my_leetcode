impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        sentence.bytes().fold(67108863, |x, y| x & !(1 << (y - 97))) == 0
    }
}
