impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.windows(2).map(|x|(x[1]-x[0]).max(0)).sum()
    }
}
