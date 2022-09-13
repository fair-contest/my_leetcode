impl Solution {
    pub fn maximum_swap(num: i32) -> i32 {
        let mut n = num;
        let mut left = (0, 0);
        let mut right = (0, 0);
        let mut prev = (0, 0);
        let mut idx = 0;
        let mut res = 0;
        while n != 0 {
            let v = (n % 10);
            if v > prev.0 {
                prev = (v, idx);
            } else if v == prev.0 {
                if idx <= left.1 { right.1 = idx;}
            } else {
                left = (v, idx);
            }
            if idx <= left.1 { right = prev;}
            res += v * 10i32.pow(idx);
            n /= 10;
            idx += 1;
        }
        // 如不需要交换，直接返回res
        if left == right || left == (0, 0) { return res;}
        // 如需要交换，从res中减去left和right交换前对应的值，再加上交换后的值即是正确答案
        res += left.0 * 10i32.pow(right.1)  + right.0 * 10i32.pow(left.1) - left.0 * 10i32.pow(left.1) - right.0*10i32.pow(right.1);
        res
    }
}
