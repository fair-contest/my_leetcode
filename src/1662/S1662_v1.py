class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = (j for i in word1 for j in i)
        b = (j for i in word2 for j in i)
        while (x := next(a, 0)) == (y := next(b, 0)):
            if x == 0 and y == 0:
                return True
        return False
