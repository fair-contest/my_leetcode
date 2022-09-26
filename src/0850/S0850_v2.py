class Solution:
    def rectangleArea(self, rectangles) -> int:
        ar, tmp = [], []
        for i in rectangles:
            i.append(self.vectArea(i))
            tmp.append(tuple(i))
        res = 0
        while len(tmp) > 1:
            tmp.sort(key=lambda x: x[4], reverse=True)
            res += tmp[0][4]
            for j in tmp[1:]:
                self.reOverlap(tmp[0], j, ar)
            if tmp == ar:
                break
            tmp = []
            tmp, ar = ar, tmp
        if len(tmp) > 0:
            for k in tmp:
                res += k[4]
        if res == 0:
            res += tmp[0][4] 
        return res % 1000000007

    def vectArea(self, x):
        area = (x[2]-x[0])*(x[3]-x[1])
        return area if area >= 0 else -area

    def pushT(self, a, b, c, d, arr):
        arr.append((a, b, c, d, abs((c-a)*(d-b))))

    def reOverlap(self, a, b, v):
        if a[0] <= b[0] and a[1] <= b[1] and a[2] >= b[2] and a[3] >= b[3]:
            return
        elif a[0] >= b[2] or a[1] >= b[3] or a[2] <= b[0] or a[3] <= b[1]:
            v.append(b)
        elif a[0] <= b[0] and a[2] >= b[2]:
            if (a[1] > b[1]):
                if a[3] < b[3]:
                    self.pushT(b[0], a[3], b[2], b[3], v)
                    self.pushT(b[0], b[1], b[2], a[1], v)
                else:
                    if a[1] < b[3]:
                        self.pushT(b[0], b[1], b[2], a[1], v)
            elif a[3] > b[1] and a[3] < b[3]:
                self.pushT(b[0], a[3], b[2], b[3], v)
        elif a[1] <= b[1] and a[3] >= b[3]:
            if a[0] > b[0]:
                if a[2] < b[2]:
                    self.pushT(a[2], b[1], b[2], b[3], v)
                    self.pushT(b[0], b[1], a[0], b[3], v)
                elif a[0] < b[2]:
                    self.pushT(b[0], b[1], a[0], b[3], v)
            elif a[2] < b[2] and a[2] > b[0]:
                self.pushT(a[2], b[1], b[2], b[3], v)
        elif a[0] > b[0]:
            if a[3] > b[3]:
                if a[2] >= b[2]:
                    self.pushT(b[0], b[1], b[2], a[1], v)
                    self.pushT(b[0], a[1], a[0], b[3], v)
                else:
                    self.pushT(b[0], b[1], b[2], a[1], v)
                    self.pushT(b[0], a[1], a[0], b[3], v)
                    self.pushT(a[2], a[1], b[2], b[3], v)
            elif a[1] < b[1]:
                if (a[2] >= b[2]):
                    self.pushT(b[0], a[3], b[2], b[3], v)
                    self.pushT(b[0], b[1], a[0], a[3], v)
                else:
                    self.pushT(b[0], a[3], b[2], b[3], v)
                    self.pushT(b[0], b[1], a[0], a[3], v)
                    self.pushT(a[2], b[1], b[2], b[3], v)
            else:
                self.pushT(b[0], b[1], a[0], b[3], v)
                self.pushT(a[0], a[3], b[2], b[3], v)
                self.pushT(a[0], b[1], b[2], a[1], v)
        else:
            if a[2] < b[2]:
                if a[3] > b[3]:
                    self.pushT(b[0], b[1], b[2], a[1], v)
                    self.pushT(a[2], a[1], b[2], b[3], v)
                elif a[1] < b[1]:
                    self.pushT(b[0], a[3], b[2], b[3], v)
                    self.pushT(a[2], b[1], b[2], a[3], v)
                else:
                    self.pushT(b[0], b[1], a[2], a[1], v)
                    self.pushT(a[2], b[1], b[2], b[3], v)
                    self.pushT(b[0], a[3], a[2], b[3], v)
