class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        strn = str(n)
        nlen = len(strn)
        dlen = len(digits)
        plist = []
        for i in range(nlen-1, 0, -1):
            plist.append(dlen**i)
        res = sum(plist)
        plist.append(1)
        i, check, opt = 0, 0, 0
        for i, v in enumerate(strn):
            check = sum(int(j)*0+1 for j in digits if int(j) <= int(v))
            if check == 0:
                break
            opt = sum(int(j)*0+1 for j in digits if int(j) < int(v))
            res += plist[i] * opt
            if check == opt:
                break
        print(plist)
        return res + check - opt if i == nlen - 1 and check != 0 else res
