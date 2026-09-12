# Problem: Best Time to Buy and Sell Stock (#121)
# Difficulty: Easy
# Date: September 12, 2026
# Note: Solved independently!

class Solution:
    def maxProfit(self, prices):
        cheapest = prices[0]
        best = 0
        for price in prices:
            profit = price - cheapest
            if profit > best:
                best = profit
            if price < cheapest:
                cheapest = price
        return best
