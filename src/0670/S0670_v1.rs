impl Solution {
    pub fn maximum_swap(num: i32) -> i32 {
        let mut n = num;
        let mut left = (0, 0);
        let mut right = (0, 0);
        let mut idx = 0;
        let mut res = 0;
        while n != 0 {
            let v = n % 10;
            if v >= right.0 {
                if idx <= left.1 {right = (v, idx);}
            } else {
                left = (v, idx);
            }
            res += v * 10i32.pow(idx);
            n = n / 10;
            idx += 1;
        }
        if left == right || left == (0, 0) { return res;}
        res += left.0 * 10i32.pow(right.1)  + right.0 * 10i32.pow(left.1) - left.0 * 10i32.pow(left.1) - right.0*10i32.pow(right.1);
        res
    }
}
