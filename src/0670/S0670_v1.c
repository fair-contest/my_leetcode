int maximumSwap(int num){
    int left[2] = {0, 0};
    int right[2] = {0, 0};
    int prev[2] = {0, 0};
    int idx = 0;
    int res = 0;
    while (num != 0) {
        int v = num % 10;
        if (v > prev[0]) {
            prev[0] = v;
            prev[1] = idx;
        } else if (v == prev[0]) {
            if (idx <= left[1]) right[1] = idx;
        } else {
            left[0] = v;
            left[1] = idx;
        }
        if (idx <= left[1]) {
            right[0] = prev[0];
            right[1] = prev[1];
        }
        res += v * pow(10, idx);
        num /= 10;
        idx += 1; 
    }
    if ((left == right) | (left[0]==0 & left[1]==0)) return res;
    res += left[0] * (pow(10, right[1]) - pow(10, left[1])) + right[0] * (pow(10, left[1]) - pow(10, right[1]));
    return res;
}
