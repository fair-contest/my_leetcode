class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        imax = values[0]
        res = imax + values[1] - 1
        for j in range(2, len(values)):
            if (s := values[j-1] + j - 1) > imax:
                imax = s
            if (s := imax + values[j] - j) > res:
                res = s
        return res
