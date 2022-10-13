func maxChunksToSorted(arr []int) int {
    rec := make([]int, len(arr)+1)
    cur := arr[0]
    p := 0
    rec[0] = 0
    for _, x := range arr {
        for {
            if x >= rec[p] {
                break
            }
            p -= 1
        }
        if x > cur {
            cur = x
        }
        p += 1
        rec[p] = cur
    }
    return p
}
