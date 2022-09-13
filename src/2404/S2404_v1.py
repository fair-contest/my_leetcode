class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        return __import__('collections').Counter(filter(lambda x: x%2 == 0, nums)).most_common(1)[0][0]
