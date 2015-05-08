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
        nums = sorted(nums)
        numsLength = len(nums)
        result, i = [], 0
        while i < numsLength - 2:
            j = i + 1
            k = numsLength - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1] : j += 1
                    while j < k and nums[k] == nums[k + 1] : k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result