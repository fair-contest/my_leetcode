class Solution:
    def getLucky(self, s: str, k: int) -> int:
        return reduce(lambda x, _: sum(map(lambda z: int(z), str(x))), range(k-1), sum(map(sum, map(lambda z: divmod(ord(z)-96, 10), s))))
