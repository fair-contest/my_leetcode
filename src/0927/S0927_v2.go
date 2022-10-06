func threeEqualParts(arr []int) []int {
	cnt := 0
	arrlen := len(arr)
	fail := []int{-1, -1}
	for v := 0; v < arrlen; v++ {
		if arr[v] == 1 {
			cnt += 1
		}
	}
	if cnt == 0 {
		return []int{0, arrlen-1}
	}
	if cnt % 3 != 0 {
		return fail
	}
	j := cnt / 3
	cnt = 0
	i := 0
	for v := arrlen - 1; v > 0; v-- {
		i += 1
		if arr[v] == 1 {
			cnt += 1
			if cnt == j {
				j = arrlen - i
				break
			}
		}
	}
	cnt = 0
	r := len(arr[j:])
	for {
		if cnt >= j {
			break
		}
		if arr[cnt] == 1 {
			break
		}
		cnt += 1
	}
	i = cnt + r - 1
	j = toInt(arr[j:])
	if toInt(arr[cnt:i+1]) != j {
		return fail
	}
	cnt = i + 1
	for {
		if cnt >= arrlen - r {
			break
		}
		if arr[cnt] == 1 {
			break
		}
		cnt += 1
	}
	if toInt(arr[cnt:cnt+r]) != j {
		return fail
	}
	return []int{i, cnt+r}
}

func toInt(arr []int) int {
	res := 0
	r := len(arr)
	d := 0
	for v := r - 1; v >= 0; v-- {
		if arr[v] == 1 {
			res += 2 << d
		}
		d += 1
	}
	return res
}
