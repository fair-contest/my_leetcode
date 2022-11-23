class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        n = int(math.log2(poured))
        r = (poured + 1) / (2 ** n) - 1
        if query_glass == 0 or query_glass == query_row:
            if query_row > n:
                return 0
            elif query_row < n:
                return 1
            else:
                return r
        else:
            row = [poured]
            for i in range(1, query_row + 1):
                next = [0] * (i + 1)
                for j, v in enumerate(row):
                    if v > 1:
                        next[j] += (v - 1) / 2
                        next[j + 1] += (v - 1) / 2
                row = next
            return min(1, row[query_glass])
