"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 23, 2015
 Problem:    Best Time to Buy and Sell Stock II
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_122
 Notes:
 Say you have an array for which the ith element is the price of a given stock on day i.
 Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
 (ie, buy one and sell one share of the stock multiple times). 
 However, you may not engage in multiple transactions at the same time 
 (ie, you must sell the stock before you buy again).

 Solution: Add all the ascending value
  """

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        increase = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
                increase += prices[i] - prices[i - 1]
        return increase