class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        rec = [None] * (len(arr)+1)
        rec[0] = 0
        cur, p = arr[0], 0
        for i in arr:
            while i < rec[p]:
                p -= 1
            p += 1
            if i > cur:
                cur = i;
            rec[p] = cur
        return p
