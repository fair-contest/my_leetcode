class Solution:
    def minSwap(self, nums1, nums2) -> int:
        s1, s2 = 0, 1
        for i in range(1, len(nums1)):
            if  nums1[i-1]<nums1[i] and nums2[i-1]<nums2[i]:
                if nums1[i-1]<nums2[i] and nums2[i-1]<nums1[i]:
                    s1 = min(s1, s2)
                    s2 = s1 + 1
                else:
                    s2 += 1
            else:
                s1, s2 = s2, s1+1
        return min(s1, s2)
