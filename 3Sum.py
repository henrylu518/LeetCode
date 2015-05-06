"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 6, 2015
 Problem:    3Sum
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_15
 Notes:
 Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
 Find all unique triplets in the array which gives the sum of zero.
 Note:
 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
 The solution set must not contain duplicate triplets.
 For example, given array S = {-1 0 1 2 -1 -4},
 A solution set is:
 (-1, 0, 1)
 (-1, -1, 2)

 Solution: enumrate a,b,  and use hash table to check for the remain c  O(n^2)
            and use sorted array to avoid duplicate work 
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1
        nums = sorted(nums)
        resultSet = set([])
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                x, y = nums[i], nums[j]
                remain = -(x + y)
                if remain == y:
                    # consider duplicate value: (x = y = remain), or (x != y and y = remain)
                    if (x == y and numsDict[remain] >= 3) or (x!= y and numsDict[remain] >= 2):
                        resultSet.add((x,y,remain))
                elif remain > y:
                    if remain in numsDict:
                        resultSet.add((x,y,remain))
        return [e for e in resultSet]