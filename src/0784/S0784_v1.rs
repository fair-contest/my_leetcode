impl Solution {
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let mut res = Vec::<String>::new();
        res.push("".to_string());
        for c in s.chars() {
            let n = res.len();
            let mut i = 0;
            if c.is_ascii_lowercase() {
                while i < n {
                    res.push(res[i].to_owned() + &c.to_ascii_uppercase().to_string());
                    res[i] = res[i].to_owned() + &c.to_string();
                    i += 1;
                }
            } else if c.is_ascii_uppercase() {
                while i < n {
                    res.push(res[i].to_owned() + &c.to_ascii_lowercase().to_string());
                    res[i] = res[i].to_owned() + &c.to_string();
                    i += 1;
                }
            } else {
                while i < n {
                    res[i] = res[i].to_owned() + &c.to_string();
                    i += 1;
                }                
            }
        }
        res
    }
}
