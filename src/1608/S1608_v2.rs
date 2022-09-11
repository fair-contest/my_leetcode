impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let mut n = nums;
        n.sort();
        let r = n.len();
        if n[0] >= r as i32 { return r as i32; }
        for i in 1..r {
            if n[(r-i)-1] < i as i32 && n[r-i] >= i as i32 {
                return i as i32;
            }
        }
        -1
    }
}
