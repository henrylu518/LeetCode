"""
 Author:     henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Climbing Stairs
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_70
 Notes:
 You are climbing a stair case. It takes n steps to reach to the top.
 Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 Solution: Clime one step + Climb two step. (like the Fibonacci sequence)
 """

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        previous, current = 0, 1
        for _ in xrange(n):
            previous, current = current, previous + current
        return current