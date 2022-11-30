class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        return min(s)[1] if (s := [(abs(a-x) + abs(b-y), i) for i, (a, b) in enumerate(points) if a == x or b == y]) else -1
