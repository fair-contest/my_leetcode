impl Solution {
    pub fn construct_array(n: i32, k: i32) -> Vec<i32> {        
        (1..n+1)
            .map(|x| Solution::gen(x, k))
            .collect::<Vec<i32>>()
    }

    pub fn gen(r: i32, k: i32) -> i32 {
        if r == 1 {
            return 1;
        }
        else if r <= k+1 {
            if r%2 == 0 {
                return 2 + k - (r / 2);
            } else {
                return (r + 1) / 2;
            }
        } else {
            return r;
        }
    }
}
