impl Solution {
    pub fn most_frequent_even(nums: Vec<i32>) -> i32 {
        let evenlist:Vec<i32> = nums.into_iter().filter(|x|x%2==0).collect();
        if evenlist.is_empty() { return -1; }
        let mut cnt = std::collections::BTreeMap::new();
        for i in evenlist.into_iter() {
            let v = cnt.entry(i).or_insert(0);
            *v += 1;
        }
        let max_cnt = cnt.iter().map(|x|x.1).max();
        *cnt.iter().filter(|x|Some(x.1) == max_cnt).map(|x|x.0).min().unwrap()
    }
}
