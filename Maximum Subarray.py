"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 13, 2015
 Problem:    Maximum Subarray
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_53
 Notes:
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 For example, given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray [4,-1,2,1] has the largest sum = 6.

 Solution: dp.
 """

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray_1(self, nums):
        largestSum, sumEndWithI = None, None
        for x in nums:
            sumEndWithI = max(x, sumEndWithI + x) if sumEndWithI else x
            largestSum = max(sumEndWithI, largestSum) 
        return largestSum

    def maxSubArray_2(self, nums):
        globalMax, localMax = None, 0
        for num in nums:
            globalMax = max(globalMax, localMax + num)
            localMax = max(0, localMax + num)
        return globalMax

    def maxSubArray_3(self, nums):
        dp, result = nums[0], nums[0]
        for num in nums[1:]:
            dp = max(num, num + dp)
            result = max(dp, result)
        return result
