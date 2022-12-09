class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return n % 3 != 2 and self.checkPowersOfThree(n // 3) if n else True
