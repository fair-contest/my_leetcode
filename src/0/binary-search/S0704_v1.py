class Solution:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            i = start + (end - start) // 2
            if target > nums[i]:
                start = i + 1
            elif target < nums[i]:
                end = i - 1
            else:
                return i
        return -1
