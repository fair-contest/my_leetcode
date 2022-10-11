class Solution {
    public int minSwap(int[] nums1, int[] nums2) {
        int s1 = 0;
        int s2 = 1;
        for (int i=1;i<nums1.length;i++) {
            if (nums1[i-1]<nums1[i] && nums2[i-1]<nums2[i]) {
                if (nums1[i-1]<nums2[i] && nums2[i-1]<nums1[i]) {
                    s1 = Math.min(s1, s2);
                    s2 = s1 + 1;
                } else { s2 += 1;}
            } else {
                s2 = s2 + s1;
                s1 = s2 - s1;
                s2 = s2 - s1 + 1;
            }
        }
        return Math.min(s1, s2);
    }
}
