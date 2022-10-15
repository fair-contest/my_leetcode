class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return i-1 if target == nums[(i := bisect.bisect(nums, target))-1] else -1
