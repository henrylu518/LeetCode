"""
 Author:     Annie Kim, anniekim.pku@gmail.com : King, higuige@gmail.com
 Date:       May 13, 2015
 Problem:    Subsets
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_78
 Notes:
 Given a set of distinct integers, S, return all possible subsets.
 Note:
 Elements in a subset must be in non-descending order.
 The solution set must not contain duplicate subsets.
 For example,
 If S = [1,2,3], a solution is:
 [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
 ]

 Solution: Recursive solution

 """

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets_1(self, nums):

        def subsetsOrder(nums):
            if nums == []: return [[]]
            s = subsetsOrder(nums[1:])
            return s + [[nums[0]] + e for e in s]
            
        return subsetsOrder(sorted(nums))

    