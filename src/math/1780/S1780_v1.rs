impl Solution {
    pub fn check_powers_of_three(n: i32) -> bool {
        let mut n = n;
        let tb: [i32; 15] = [4782969, 1594323, 531441, 177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1];
        for &i in tb.iter() {
            if n >= i {
                if i == n {break;}
                if 1 + ((3 * i - 3) >> 1) < n {return false;}
                n -= i;
            }
        }
        true
    }
}
