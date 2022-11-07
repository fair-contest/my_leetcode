class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        old = image[sr][sc]
        if color == old:
            return image
        m, n = len(image), len(image[0])
        dq = deque([(sr, sc)])
        while dq:
            p = dq.popleft()
            image[p[0]][p[1]] = color
            for i in ((p[0]+1, p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)):
                if i[0] < 0 or i[1] < 0 or i[0] == m or i[1] == n or image[i[0]][i[1]] != old:
                    continue
                dq.append(i)
        return image
