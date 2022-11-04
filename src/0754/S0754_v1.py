class Solution:
    def reachNumber(self, target: int) -> int:
        return n if (t:=abs(target)) == (s:=(n:=round((2*t)**0.5))*(n+1)>>1) or s-t&1 == 0 else n+1+(n&1)
