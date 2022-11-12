class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = [0] * 26
        for i in s:
            cnt[ord(i)-97] += 1
        res = ''
        for j in order:
            while cnt[ord(j)-97] != 0:
                res += j
                cnt[ord(j)-97] -= 1
        for i, v in enumerate(cnt):
            while v != 0:
                res += chr(i+97)
                v -= 1
        return res
