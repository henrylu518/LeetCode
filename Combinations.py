"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 13, 2015
 Problem:    Combinations
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_77
 Notes:
 Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
 For example,
 If n = 4 and k = 2, a solution is:
 [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
 ]

 Solution: DFS.
 """

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}

    def combine_1(self, n, k):
        def combineRecur(result, current, m, remain):
            if remain == 0: 
                result.append(current)
                return
            if m > 0:
                combineRecur(result, [m] + current , m - 1, remain - 1)
                combineRecur(result, current, m - 1, remain)

        result = []
        combineRecur(result,[], n, k)
        return result

    def combine_2(self, n, k):
        def combineRecur(current, m, remain):
            if remain == 0: return [current]
            if m > 0:
                return combineRecur( [m] + current, m - 1, remain - 1) + \
                combineRecur(current, m - 1, remain)
            return []

        return combineRecur([], n, k )

