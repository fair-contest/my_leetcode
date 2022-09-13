class Solution:
    def maximumSwap(self, num: int) -> int:
        left, right, prev = [0, 0], [0, 0], [0, 0]
        idx, res = 0, 0
        while num != 0:
            v = num % 10
            if v > prev[0]:
                prev = (v, idx)
            elif v == prev[0]:
                if idx <= left[1]:
                    right[1] = idx
            else:
                left = (v, idx)
            if idx <= left[1]:
                right = prev
            res += v * (10**idx)
            num //= 10
            idx += 1
        if left == right or left == (0, 0):
            return res
        res += left[0] * (10**right[1] - 10**left[1]) + right[0] * (10**left[1] - 10**right[1])
        return res
