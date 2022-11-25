class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(1 for i in words if self.isStretchy(s, i))

    def isStretchy(self, s: str, word: str) -> bool:
        i, j = 0, 0
        m, n = len(s), len(word)
        while i < n and j < m:
            cmp = s[j]
            if word[i] != cmp:
                return False
            cnt1, cnt2 = 1, 1
            while (i := i + 1) < n and word[i] == cmp:
                cnt1 += 1
            while (j := j + 1) < m and s[j] == cmp:
                cnt2 += 1
            if cnt2 < cnt1 or (cnt2 == 2 and cnt1 == 1):
                return False
        if i != n or j != m:
            return False
        return True
