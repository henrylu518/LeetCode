"""
 Author:     henry, henrylu518@gmail.com
 Date:       May 23, 2015
 Problem:    Best Time to Buy and Sell Stock III
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_123
 Notes:
 Say you have an array for which the ith element is the price of a given stock on day i.
 Design an algorithm to find the maximum profit. You may complete at most two transactions.
 Note:
 You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

 Solution: dp. max profit =  max profit of left + max profit of right
 """

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if prices == []: return 0
        maxProfitLeft = [None] * len(prices)
        maxProfitRight = [None] * len(prices)
        minPrice, maxProfitLeft[0] = prices[0], 0
        for i in xrange(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfitLeft[i] = max( maxProfitLeft[i - 1], prices[i] - minPrice )
        maxPrice, maxProfitRight[-1] = prices[-1], 0
        for i in xrange(len(prices) - 2, -1, -1):
            maxPrice = max(prices[i], maxPrice)
            maxProfitRight[i] = max(maxProfitRight[i + 1], maxPrice - prices[i])
        return max([maxProfitLeft[i] + maxProfitRight[i]  for i in xrange(len(prices))])