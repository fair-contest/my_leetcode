impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack.len() == 0 || needle.len() == 0 { return 0; }
        let mut res = 0;
        for i in haystack.as_bytes().windows(needle.len()) {
            if &i == &needle.as_bytes() { return res; }
            res += 1;
        }
        -1
    }
}
