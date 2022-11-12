class Solution:
    def numTilings(self, n: int) -> int:
        s, prev, pprev = 0, 1, 1
        cur = 1
        for i in range(2, n+1):
            cur = (s + prev + pprev) % 1000000007
            s += pprev << 1
            pprev = prev
            prev = cur
        return cur
