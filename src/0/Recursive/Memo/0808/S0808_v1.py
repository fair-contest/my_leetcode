class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4275: return 0.99999
        n = n * 0.01
        @cache
        def dfs(a: float, b: float) -> float:
            if a <= 0:
                if b <= 0:
                    return 0.5
                else:
                    return 1.0
            elif b <= 0:
                return 0.0
            return 0.25 * (dfs(a-1, b) + dfs(a-0.75, b-0.25) + dfs(a-0.5, b-0.5) + dfs(a-0.25, b-0.75))

        return dfs(n, n)
