class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m > n * 6 or n > m * 6:
            return -1
        gap = sum(nums1) - sum(nums2)
        if gap == 0:
            return 0
        a, b = Counter(nums1), Counter(nums2)
        def cnt_res(a, b, gap):
            res = 0
            for i in range(6, 0, -1):
                s = a[i] * (i - 1)
                if gap <= s:
                    res += ceil(gap / (i - 1))
                    break
                else:
                    res += a[i]
                    gap -= s
                s = b[7-i] * (i - 1)
                if gap <= s:
                    res += ceil(gap / (i - 1))
                    break
                else:
                    res += b[7-i]
                    gap -=s
            return res
        return cnt_res(a, b, abs(gap)) if gap > 0 else cnt_res(b, a, abs(gap))
