class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 如果mines个数和矩形总元素个数一样，代表所有点都是0
        if len(mines) == n * n:
            return 0

        # 从mines给边长为n的矩阵matrix填0
        matrix = [[1]*(n) for _ in range(n)]
        for i in mines:
            matrix[i[0]][i[1]] = 0
        
        def calcCross(x: int, y: int, cmp: int):
            # 从可能形成十字架的中点坐标集模拟求解该点能形成的最大十字架阶数
            # calcCross参数的前两个值是最长连续1的中点坐标
            # 最后的值是该中点能形成的最大“轴对称”加号的阶数
            cnt = 1
            while cnt < cmp:
                if x + cnt >= n or x - cnt < 0:
                    break  
                if matrix[x+cnt][y] == 0 or matrix[x-cnt][y] == 0:
                    break
                cnt += 1
            return cnt

        # 统计matrix横轴最长连续1的中点坐标，连续1长度小于3的可省略
        res = 1
        for i, r in enumerate(matrix):
            cnt = 0
            for j, v in enumerate(r):
                if v:
                    cnt += 1
                    if j == n - 1:
                        if cnt < 3:
                            cnt = 0
                            continue
                        k = 1
                        while k < cnt - 1:
                            ck = min(k, cnt-k-1)+1
                            if ck <= res: # 当前可形成阶数不大于已求出最大值的可省略
                                k += 1
                                continue
                            res = max(res, calcCross(i, j-k, ck))
                            k += 1
                else:
                    if cnt < 3:
                        cnt = 0
                        continue
                    k = 2
                    while k < cnt:
                        ck = min(k-1, cnt-k)+1
                        if ck <= res: # 当前可形成阶数不大于已求出最大值的可省略
                            k += 1
                            continue
                        res = max(res, calcCross(i, j-k, ck))
                        k += 1
                    cnt = 0
        return res
