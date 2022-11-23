class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0: return 0
        elif poured == 1: return 0 if query_row != 0 or query_glass != 0 else 1
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
            if poured == 2 and query_row > 1: return 0
            row = [(poured - 3) * 0.5]
            edge = (((poured - 3) * 0.25) - 1) * 0.5
            for i in range(2, query_row):
                next = [0] * i
                if i < n - 1:
                    next[0], next[-1] = edge, edge
                    edge = (edge - 1) * 0.5
                elif i == n - 1:
                    next[0], next[-1] = r, r
                for j, v in enumerate(row):
                    if v > 1:
                        next[j] += (v - 1) * 0.5
                        next[j + 1] += (v - 1) * 0.5
                row = next
            return min(1, row[query_glass - 1])
