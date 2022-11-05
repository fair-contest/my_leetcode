class Solution {
    public int reachNumber(int target) {
        if (target < 0) target = -target;
        int n = (int)(Math.sqrt(target<<1) + 0.5);
        int s = n * n + n >> 1;
        return ((s - target & 1) == 0  || s == target) ? n : n + 1 + (n&1);
    }
}
