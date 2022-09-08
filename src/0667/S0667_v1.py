class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        return [res for res in self.gen(n, k)]

    def gen(self, n, k):
        yield 1
        res = 1
        for i in range(k, 0, -1):
            if k%2 == 0:
                res = res + i if i%2 == 0 else res - i
            else:
                res = res + i if i%2 == 1 else res - i
            yield res

        for j in range(k+2, n+1):
            yield j
