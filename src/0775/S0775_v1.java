class Solution {
    public boolean isIdealPermutation(int[] nums) {
        return IntStream.rangeClosed(0, nums.length - 1).noneMatch(i -> Math.abs(i - nums[i]) > 1);
        // return (IntStream.rangeClosed(0, nums.length - 1).anyMatch(i -> Math.abs(i - nums[i]) > 1)) ? false : true;
    }
}
