func maxScoreSightseeingPair(values []int) int {
    res, imax := 0, 0
    for i := range values {
        res = max(res, imax + values[i])
        if values[i] > imax {
            imax = values[i]
        }
        imax--
    }
    return res
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
