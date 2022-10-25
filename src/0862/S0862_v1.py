class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        i, j, s = 0, 0, 0
        n = len(nums)
        res, tmp = n + 1, 0
        while j < n:
            s += nums[j]
            while s > k:
                s -= nums[i]
                i += 1
            if s == k:
                tmp = j - i + 1
                if tmp < res:
                    res = tmp
            j += 1
        return res if res != n + 1 else -1
