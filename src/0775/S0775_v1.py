class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return False if any(1 for i, v in enumerate(nums) if abs(i - v) > 1) else True
