class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        imax = values[0]
        res = 0
        for i in values[1:]:
            imax -= 1
            if (s := imax + i) > res:
                res = s
            if i > imax:
                imax = i
        return res
