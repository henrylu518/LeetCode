"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 17, 2015
 Problem:    4Sum
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_18
 Notes:
 Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
 Find all unique triplets in the array which gives the sum of zero.
 Note:
 Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
 Find all unique quadruplets in the array which gives the sum of target.
 Note:
 Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
 The solution set must not contain duplicate quadruplets.
 For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
 A solution set is:
 (-1,  0, 0, 1)
 (-2, -1, 1, 2)
 (-2,  0, 0, 2)

 Solution: Similar to 3Sum, 2Sum.
            Add constrains to make it faster.
 """

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        for i in xrange(len(nums) - 3):
            if nums[i] > target / 4.0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            threeSum = target - nums[i]
            for j in xrange(i + 1, len(nums) - 2):
                if nums[j] > threeSum / 3.0: break
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                twoSum = threeSum - nums[j]
                m, n = j + 1, len(nums) - 1
                if nums[m] > twoSum / 2.0 or nums[n] < twoSum / 2.0 : continue
                while m < n:
                    tSum = nums[m] + nums[n]
                    if tSum  == twoSum:
                        result.append((nums[i], nums[j], nums[m], nums[n]))
                        mm, nn = nums[m], nums[n]
                        while m < n and nums[m + 1] == mm: m += 1
                        while m < n and nums[n - 1] == nn: n -= 1
                        m += 1; n -= 1
                    elif tSum > twoSum:
                        n -= 1
                    else:
                        m += 1
        return result

