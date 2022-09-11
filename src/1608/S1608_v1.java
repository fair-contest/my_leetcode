class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int r = nums.length;
        if (nums[0] >= r) { return r; }
        for (int i=1; i<r; i++) {
            if (nums[r-i] >= i && (nums[(r-i)-1] < i)) {
                return i;
            }
        }
        return -1;
    }
}
