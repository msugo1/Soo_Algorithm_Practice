# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# only when Greedy_Algorithm yields the best result
# 1. Optimal Substructure - an optimal solution to the problem contains optimal solutions to the sub-problems
# 2. Greedy Choice Property - pick out whatever choice seems best at the moment
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        stock_price = prices[0]

        # have a look from the second element because the first one is already set as a current price
        for i in range(1, len(prices)):   
            # if our stock price is more expensive than current price, swap the two with each other
            if prices[i] < stock_price:
                stock_price = prices[i]

            # if not, sell the stock from the previous price(i - 1]), add the profit to the total, and buy a new one
            # (could be more elaborated as "if current_price(prices[i]) > stock_price
            # and current_price > previous_price(prices[i - 1])")
            else:
                total_profit += prices[i] - stock_price
                stock_price = prices[i]

        return total_profit

# result - runtime: 60ms(83.34%), memory usage: 15MB(86.41%)
# time complexity - O(n) with a linear loop
# space complexity - O(n) with two variables

# been quite frustrated with not being able to solve problems on my own for the last couple of days (especially those sliding window problems)
# This question was a real confident booster

# Solutions from Python Algorithm Interview
# 1) just sell it whenever the price of the next day is more expensive

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]

        return result
# more consise and precise and even 99.79 and 99.24 in runtime and memory usage each

# 2) more pythonic way

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[1 + i] - prices[i], 0) for i in range(len(prices) - 1))

# the result can be added to the total profit as long as it is above 0
# How on earth can a person think of such solution like this!!!
# I need way more practice to reach this level
