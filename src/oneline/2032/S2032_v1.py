class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list(((s1 := set(nums1)) & (s2 := set(nums2))) | (s2 & (s3 := set(nums3))) | (s1 & s3))
