class Solution {
    public boolean checkPowersOfThree(int n) {
        int[] tb = {4782969, 1594323, 531441, 177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1};
        for (int i = 0;i < 15;++i) {
            if (n >= tb[i]) {
                if (tb[i] == n) break;
                if (1 + ((3 * tb[i] - 3) >> 1) < n) return false;
                n -= tb[i];
            }
        }
        return true;
    }
}
