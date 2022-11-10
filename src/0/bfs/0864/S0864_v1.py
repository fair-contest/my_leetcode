class Solution:
    def shortestPathAllKeys(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        need_keys = 0
        x = (0, 0)
        for i in product(range(m), range(n)):
            if (k := ord(grid[i[0]][i[1]]) - 97) >= 0 and k <= 6:
                need_keys = need_keys | (1 << k) # 将need_keys的第k位设为1
            if grid[i[0]][i[1]] == '@':
                x = (i[0], i[1])
        x = (x[0], x[1], 0)
        step, choice = 0, 0
        nxt = deque()
        passed = {x}
        while 1:
            c = x[2]
            if (k := ord(grid[x[0]][x[1]]) - 97) >= 0 and k <= 6:
                c = c | (1 << k) # 将c的第k位设为1
                if c == need_keys:
                    return step
            def passLock(x: int, y: int, keys: int) -> bool:
                if (lock := ord(grid[x][y]) - 65) >= 0 and lock <= 6:
                    # 将1左移lock-1位，相当于变成只有第i位上是1，其他位上都是0的二进制数。
                    # 然后与keys做与运算，如结果>0，说明keys第lock位上是1，key与lock匹配。
                    return True if ((1 << lock) & keys) > 0 else False
                return True
            if (t:=x[0]+1) < m and grid[t][x[1]] != '#' and passLock(t, x[1], c):
                if (t, x[1], c) not in passed:
                    passed.add((t, x[1], c))
                    nxt.append((t, x[1], c))
            if (t:=x[0]-1) >= 0 and grid[t][x[1]] != '#' and passLock(t, x[1], c):
                if (t, x[1], c) not in passed:
                    passed.add((t, x[1], c))
                    nxt.append((t, x[1], c))
            if (t:=x[1]-1) >= 0 and grid[x[0]][t] != '#' and passLock(x[0], t, c):
                if (x[0], t, c) not in passed:
                    passed.add((x[0], t, c))
                    nxt.append((x[0], t, c))
            if (t:=x[1]+1) < n and grid[x[0]][t] != '#' and passLock(x[0], t, c):
                if (x[0], t, c) not in passed:
                    passed.add((x[0], t, c))
                    nxt.append((x[0], t, c))
            if choice == 0:
                choice = len(nxt)
                step += 1         
            if nxt:
                x = nxt.popleft()
                choice -= 1
            else:
                break
        return -1
