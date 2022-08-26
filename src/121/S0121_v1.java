class Solution {
    public int maxProfit(int[] prices) {
        int maxp = prices[0];
        int minp = prices[0];
        int res = 0;
        for(int i=0;i<prices.length;i++) {
            if (prices[i] < minp) {
                minp = prices[i];
                maxp = prices[i];
            }
            if (prices[i] > maxp) { maxp = prices[i]; }
            res = Math.max((maxp - minp), res);
        }
        return res;
    }
}
