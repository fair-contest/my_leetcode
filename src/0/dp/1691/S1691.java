class Solution {
    public int maxHeight(int[][] cuboids) {
        int[][] dp = cuboids;
        for (int[] i: dp) {
            Arrays.sort(i);
        }
        Arrays.sort(dp, (x, y) -> x[0] != y[0] ? x[0] - y[0] : x[1] != y[1] ? x[1] - y[1] : x[2] - y[2]);
        int res = 0, i = 0, s = 0;
        for (int[] v: dp) {
            v[0] = v[2];
            for (int j=0;j < i;++j) {
                if (dp[j][1] <= v[1] && dp[j][2] <= v[2]) {
                    if (dp[j][0] > s) { s = dp[j][0];}
                }
            }
            v[0] += s;
            s = 0;
            if (v[0] > res) {res = v[0];}
            i++;
        }
        return res;
    }
}
