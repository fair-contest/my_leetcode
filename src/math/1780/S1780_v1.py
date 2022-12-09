class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        tb = (4782969, 1594323, 531441, 177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1)
        for i in tb:
            if n >= i:
                if i == n:
                    return True
                if 1 + ((3 * i - 3) >> 1) < n:
                    return False
                n -= i
