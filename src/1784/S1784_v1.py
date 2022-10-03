class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return (int(s, 2) ^ int(s, 2)>>1).bit_count() <= 2
