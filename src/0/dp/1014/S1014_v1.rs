impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        let mut imax = 0;
        let mut res = 0;
        for &i in values.iter() {
            res = res.max(imax + i);
            if i > imax {imax = i;}
            imax -= 1;
        }
        res
    }
}
