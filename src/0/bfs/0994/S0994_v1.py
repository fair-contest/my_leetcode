class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        dq = deque()
        for i in product(range(m), range(n)):
            if grid[i[0]][i[1]] == 1:
                fresh += 1
            if grid[i[0]][i[1]] == 2:
                dq.append((i[0], i[1]))
        if fresh == 0:
            return 0
        r, minutes = len(dq), 1
        while dq:
            r -= 1
            p = dq.popleft()
            for i in ((p[0]+1, p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)):
                if i[0] < 0 or i[1] < 0 or i[0] == m or i[1] == n or grid[i[0]][i[1]] != 1:
                    continue
                fresh -= 1
                if fresh == 0:
                    return minutes
                grid[i[0]][i[1]] = 2
                dq.append(i)
            if r == 0:
                r = len(dq)
                minutes += 1
        return -1
