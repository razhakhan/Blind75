class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum_price_till_now = 999999
        n = len(prices)
        for i in range(n):
            if prices[i]<minimum_price_till_now:
                minimum_price_till_now = prices[i]
            else:
                curr_profit = prices[i] - minimum_price_till_now
                if curr_profit>max_profit:
                    max_profit = curr_profit
        return max_profit
