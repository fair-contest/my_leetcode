class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        return sum(self.gen(sorted(pairs, key=lambda x: x[1]), -inf))

    def gen(self, list, val):
        for a, b in list:
            if val < a:
                val = b
                yield 1
