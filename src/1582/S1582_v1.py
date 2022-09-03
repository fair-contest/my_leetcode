class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        tmp = mat[0]
        for i in mat[1:]:
            if sum(i) == 1: # 筛出每行只有1个1的行
                tmp = list(map(lambda x, y: x + y, tmp, i)) # 将矩阵所有列相加
        return sum(filter(lambda x: x == 1, tmp)) # tmp中有多少个1，即有多少个特殊位置
