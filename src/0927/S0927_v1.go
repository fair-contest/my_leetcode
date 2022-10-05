func threeEqualParts(arr []int) []int {
	cnt := 0
	r := len(arr)
	fail := []int{-1, -1}
	for v := 0; v < r; v++ {
		if arr[v] == 1 {
			cnt += 1
		}
	}
	if cnt == 0 {
		return []int{0, r-1}
	}
	if cnt % 3 != 0 {
		return fail
	}
	j := cnt / 3
	cnt = 0
	i := 0
	for v := r - 1; v > 0; v-- {
		i += 1
		if arr[v] == 1 {
			cnt += 1
			if cnt == j {
				j = r - i
				break
			}
		}
	}
	cnt = 0
	for {
		if cnt >= j {
			break
		}
		if arr[cnt] == 1 {
			break
		}
		cnt += 1
	}
	r = len(arr[j:])
	i = cnt + r - 1
	if notEqual(arr[cnt:i+1], arr[j:]) {
		return fail
	}
	cnt = i + 1
	for {
		if cnt >= j {
			break
		}
		if arr[cnt] == 1 {
			break
		}
		cnt += 1
	}
	if notEqual(arr[cnt:cnt+r], arr[j:]) {
		return fail
	}
	return []int{i, cnt+r}
}

func notEqual(x []int, y []int) bool {
	for v := 0; v < len(x); v++ {
		if x[v] != y[v] {
			return true
		}
	}
	return false
}
