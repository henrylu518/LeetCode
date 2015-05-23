"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 23, 2015
 Problem:    Best Time to Buy and Sell Stock
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_121
 Notes:
 Say you have an array for which the ith element is the price of a given stock on day i.
 If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
 design an algorithm to find the maximum profit.

 Solution: For each element, calculate the max difference with the former elements.
 """


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        maximumProfit, minPrice = 0, float("Inf")
        for price in prices:
            minPrice = min(minPrice, price)
            maximumProfit = max(maximumProfit, price - minPrice)
        return maximumProfit


    def maxProfit_2(self, prices):
        if prices == []: return 0
        maxList = [0] * len(prices)
        for i in xrange(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                maxList[i] = prices[i]
            else:
                maxList[i] = max(maxList[i + 1], prices[i])
        return max([maxList[i] - prices[i] for i in xrange(len(prices))])