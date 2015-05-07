"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 7, 2015
 Problem:    Pow(x, n)
 Difficulty: easy
 Source:     http://leetcode.com/onlinejudge#question_50
 Notes:
 Implement pow(x, n).
 
 Solution: recursion.
 """

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0: return 1
        elif n < 0: return 1.0 / self.myPow(x, -n)
        elif n % 2 == 0: return self.myPow(x, n / 2) ** 2
        elif n % 2 == 1: return self.myPow(x, n / 2) ** 2 * x
        else: return None