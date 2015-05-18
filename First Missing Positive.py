"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    First Missing Positive
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_41
 Notes:
 Given an unsorted integer array, find the first missing positive integer.
 For example,
 Given [1,2,0] return 3,
 and [3,4,-1,1] return 2.
 Your algorithm should run in O(n) time and uses constant space.

 Solution: Although we can only use constant space, we can still exchange elements within input A!
           Swap elements in A and try to make all the elements in A satisfy: A[i] == i + 1.
           Pick out the first one that does not satisfy A[i] == i + 1.
 """

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


    def firstMissingPositive_2(self, nums):
        nums = set(nums)
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1
            