class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            l = prices[left]
            r = prices[right]

            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                prices[left] = prices[right]
            right += 1
        return profit
