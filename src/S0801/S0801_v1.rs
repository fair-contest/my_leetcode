impl Solution {
    pub fn min_swap(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut s1 = 0;
        let mut s2 = 1;
        for i in 1..nums1.len() {
            if nums1[i-1]<nums1[i] && nums2[i-1]<nums2[i] {
                if nums1[i-1]<nums2[i] && nums2[i-1]<nums1[i] {
                    s1 = std::cmp::min(s1, s2);
                    s2 = s1 + 1;
                } else { s2 += 1;}
            } else {
                std::mem::swap(&mut s1, &mut s2);
                s2 += 1;
            }
        }
        std::cmp::min(s1, s2)
    }
}
