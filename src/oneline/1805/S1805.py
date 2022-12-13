class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(lambda x: int(x), re.findall('\d+', word))))
