int reachNumber(int target){
    if (target < 0) target = -target;
    int n = sqrt(target<<1) + 0.5;
    int s = n * n + n >> 1;
    return (s == target || (s - target & 1) == 0) ? n : n + 1 + (n&1);
}
