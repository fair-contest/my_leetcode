class Solution:
    def trimMean(self, arr: List[int]) -> float:
        r = len(arr) // 20
        heap_min, heap_max = [-1 * x for x in arr[:r]], arr[r:2*r]
        heapify(heap_min)
        heapify(heap_max)
        i = 2 * r
        sum = self.ex_heap(heap_max, heap_min, arr[i])
        i += 1
        for _ in range(r-1):
            sum = self.ex_heap(heap_max, heap_min, sum)
        while i < len(arr):
            print(sum, heap_max, heap_min)
            sum += self.ex_heap(heap_max, heap_min, arr[i])
            i += 1
        return sum / (len(arr) - 2 * r)

    def ex_heap(self, h_max:list, h_min:list, v):
        return heappushpop(h_max, -1 * heappushpop(h_min, -1 * v))
