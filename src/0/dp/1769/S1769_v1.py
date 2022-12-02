class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [-boxes.count('1')] * len(boxes)
        res[0] = 0
        for i, c in enumerate(boxes):
            if c == '1':
                res[0] += i
        cnt = 0 if boxes[0] == '0' else 1
        for i in range(1, len(boxes)):
            res[i] += res[i-1] + (cnt << 1)
            if boxes[i] == '1':
                cnt += 1
        return res

"""
可观察到答案数组每个位置i相对比位置i-1，i左边每个1加了1，右边每个1减少了1，状态转移方程可写为：
dp[i] = dp[i-1] + (位置i左边的1总数) - (位置i右边的1的总数)

上式也可以写为 dp[i] = dp[i-1] + 2 * (位置i左边的1总数) - (字符串中1的总数)

所以可以直接用 - (字符串中1的总数) 来初始化答案数组。 然后按上面逻辑求解并返回答案数组。

时间复杂度：O(n), n为字符串长度。
空间复杂度：O(n)
"""
