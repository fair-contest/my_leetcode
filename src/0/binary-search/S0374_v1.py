class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            i = start + (end - start) // 2
            pick = guess(i)
            if pick == 1:
                start = i + 1
            elif pick == -1:
                end = i - 1
            else:
                return i
