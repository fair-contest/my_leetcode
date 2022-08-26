class Solution {
    public int maxProfit(int[] prices) {
        int maxp = prices[0];
        int minp = prices[0];
        int res = 0;
        for (int i : prices) {
            if (i < minp) {
                minp = i;
                maxp = i;
            }
            if (i > maxp) { maxp = i; }
            res = Math.max((maxp - minp), res);
        }
        return res;
    }
}
