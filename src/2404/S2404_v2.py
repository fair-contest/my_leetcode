class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        return min(k for k, v in c.items() if v == c.most_common(1)[0][1]) if (c := Counter(filter(lambda x: x%2 == 0, nums))) else -1
