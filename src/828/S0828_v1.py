class Solution:
    def uniqueLetterString(self, s: str) -> int:
        cmap = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        lst = [[-1] * 2 for _ in range (26)]
        res = 0
        tmp = 0
        for i in range(len(s)):
            x, y = lst[cmap[s[i]]][0], lst[cmap[s[i]]][1]
            tmp += (i - y) - (y - x)
            res += tmp
            lst[cmap[s[i]]][0] = y
            lst[cmap[s[i]]][1] = i
        return res
