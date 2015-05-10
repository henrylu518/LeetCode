"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 9, 2015
 Problem:    Remove Element
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_27
 Notes:
 Given an array and a value, remove all instances of that value in place and return the new length.
 The order of elements can be changed. It doesn't matter what you leave beyond the new length.

 Solution: 
 """

lass Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        numsLen = len(nums)
        i = 0
        while i < numsLen:
            if nums[i] == val:
                nums[i], nums[numsLen - 1] = nums[numsLen - 1], nums[i]
                numsLen -= 1
            else:
                i += 1
        return numsLen