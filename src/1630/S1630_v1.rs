impl Solution {
    pub fn check_arithmetic_subarrays(nums: Vec<i32>, l: Vec<i32>, r: Vec<i32>) -> Vec<bool> {
        let mut res = Vec::new();
        'out: for i in 0..l.len() {
            let mut tmp = nums[l[i] as usize..=r[i] as usize].to_owned();
            tmp.sort_unstable();
            for j in 2..tmp.len() {
                if tmp[j] - tmp[j-1] != tmp[1] - tmp[0] { res.push(false); continue 'out; }
            }
            res.push(true);
        }
        res
    }
}
