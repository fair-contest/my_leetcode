class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for c in s:
            n = len(res)
            i = 0
            if c.isupper():
                while i < n:
                    res.append(res[i]+c.lower())
                    res[i] += c
                    i += 1
            elif c.islower():
                while i < n:
                    res.append(res[i]+c.upper())
                    res[i] += c
                    i += 1
            else:
                while i < n:
                    res[i] += c
                    i += 1
        return res
