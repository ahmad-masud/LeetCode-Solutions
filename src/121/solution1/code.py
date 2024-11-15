class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        res = 0

        while sell < len(prices):
            res = max(res, prices[sell] - prices[buy])

            if prices[buy] > prices[sell]:
                buy = sell
            
            sell += 1

        return res