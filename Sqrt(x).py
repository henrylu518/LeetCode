"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 13, 2015
 Problem:    Sqrt(x)
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_69
 Notes:
 Implement int sqrt(int x).
 Compute and return the square root of x.

 Solution: Binary search in range [0, x / 2 + 1].
           There is also Newton iteration method. 
 """

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x < 0: return -1
        low, high = 0, x
        while high >= low:
            middle = (high + low) / 2
            if middle ** 2 == x: return middle
            elif middle ** 2 > x:
                high = middle - 1
            else:
                low = middle + 1
        return high

