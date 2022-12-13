class Solution {
    int imax, tmp, res;
    public int maxScoreSightseeingPair(int[] values) {
        imax = 0;
        res = 0;
        for (int i : values) {
            tmp = imax + i;
            if (tmp > res) res = tmp;
            if (i > imax) imax = i;
            imax--;
        }
        return res;
    }
}
