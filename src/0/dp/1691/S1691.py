class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for i in cuboids:
            i.sort()
        dp = sorted(cuboids)
        for i, v in enumerate(dp):
            dp[i] = (v[2], v[1], v[2])
            for j in dp[:i]:
                if j[1] <= v[1] and j[2] <= v[2]:
                    if (s := j[0] + v[2]) > dp[i][0]:
                        dp[i] = (s, v[1], v[2])
        return max(dp)[0]

# 下面这种写法更简洁，不过上面的写法比较容易将dp[i]作为一组整体来理解。
# dp[i][1]和dp[i][2]虽然和原来的cuboids数组中的值一样，但从动态规划角度其代表的意义不一样。

"""
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for i in cuboids:
            i.sort()
        dp = sorted(cuboids)
        for i, v in enumerate(dp):
            s = 0
            for j in dp[:i]:
                if j[1] <= v[1] and j[2] <= v[2]:
                    if j[0] > s:
                        s = j[0]
            v[0] = s + v[2]
        return max(dp)[0]
"""
