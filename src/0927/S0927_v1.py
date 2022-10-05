class Solution:
    def threeEqualParts(self, arr):
        cnt = arr.count(1)
        if cnt == 0:
            return [0, len(arr)-1] # 全是0时i, j取头尾
        if cnt % 3 != 0:
            return [-1, -1] # 1的数量不能被3整除即不可能被3等分
        j = cnt // 3
        cnt, i = 0, 0
        for v in arr[::-1]:
            i += 1
            if v == 1:
                cnt += 1
                if cnt == j:
                    j = len(arr) - i
                    break
        cnt = 0
        while cnt < j:
            if arr[cnt] == 1:
                break
            cnt += 1
        r = len(arr[j:])
        i = cnt + r - 1
        if arr[cnt:i+1] != arr[j:]:
            return [-1, -1]
        cnt = i + 1
        while cnt < j:
            if arr[cnt] == 1:
                break
            cnt += 1
        if arr[cnt:cnt+r] != arr[j:]:
            return [-1, -1]
        return [i, cnt+r]
