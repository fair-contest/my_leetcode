impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let m = sequence.len();
        let n = word.len();
        if m < n {return 0;}
        let mut res = 0;
        if sequence.contains(&word) {res = 1;} else {return 0};
        let mut i = n;
        let j = m - n + 1;
        while i < j {
            let mut cur = if &sequence[i-n..i] != &word {0} else {1};
            if &sequence[i..i+n] == &word {
                cur += 1;
                i += n;
                while i < j && &sequence[i..i+n] == &word {
                    cur += 1;
                    i += n;
                }
            } else {
                i += 1;
            }
            if cur > res {res = cur;}
        }
        res
    }
}
