class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        tmp = mat[0]
        sp = [0] if sum(tmp) == 1 else []
        res = 0

        for i, x in enumerate(mat[1:]):
            if sum(x) == 1:
                sp.append(i+1)
            tmp = list(map(lambda x, y: x + y, tmp, x))

        for j, x in enumerate(tmp):
            if x == 1:
                for i in sp:
                    if mat[i][j] == 1:
                        res += 1
        return res
