class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        return min(filter(lambda x:x[1] == r.most_common(1)[0][1], r.most_common()))[0] if (r := __import__('collections').Counter(filter(lambda x: x%2 == 0, nums))) else -1
