class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = {}
        rep = 0
        a, b = 0, 0
        for i in cpdomains:
            [rep, a] = i.split(' ', 1)
            rep = int(rep)
            if a not in cnt:
                cnt[a] = rep
            else:
                cnt[a] += rep
            [_, a] = a.split('.', 1)
            if a not in cnt:
                cnt[a] = rep
            else:
                cnt[a] += rep
            b = a.split('.', 1)
            if len(a) == len(b[0]):
                continue
            else:
                if b[1] not in cnt:
                    cnt[b[1]] = rep
                else:
                    cnt[b[1]] += rep
        return [str(cnt[k]) + ' ' + k for k in cnt]
