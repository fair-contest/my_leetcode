class Solution:
    def trimMean(self, arr: List[int]) -> float:
        return (sum(arr) - sum(nlargest(len(arr)*5//100, arr)) - sum(nsmallest(len(arr)*5//100, arr))) / (len(arr) * 0.9)
