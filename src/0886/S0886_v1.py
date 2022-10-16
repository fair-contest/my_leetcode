class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        chk = {}        
        que = deque()
        for [a, b] in dislikes:
            if chk.get(a) == None:
                chk[a] = [b]
            else:
                chk[a].append(b)
            if chk.get(b) == None:
                chk[b] = [a]
            else:
                chk[b].append(a)
        for k in [i for i in chk.keys()]:
            if len(chk[k]) == 1:
                del chk[k]
            else:
                que.append((k, chk[k]))
        if not chk:
            return True
        chk = {}
        (k, v) = que.popleft()
        chk[k] = 0
        for i in v:
            chk[i] = 1
        while que:
            (k, v) = que.popleft()
            if chk.get(k) == None:
                que.append((k, v))
            else:
                if chk[k] == 0:
                    for i in v:
                        if chk.get(i) == None:
                            chk[i] = 1
                        else:
                            if chk[i] == 0:
                                return False
                else:
                    for i in v:
                        if chk.get(i) == None:
                            chk[i] = 0
                        else:
                            if chk[i] == 1:
                                return False
        return True
