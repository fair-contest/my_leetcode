class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [left, right] if (left := bisect_left(nums, target)) <= (right := bisect_right(nums, target)-1) else [-1, -1]
