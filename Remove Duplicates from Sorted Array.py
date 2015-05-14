"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Remove Duplicates from Sorted Array
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_26
 Notes:
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
 Do not allocate extra space for another array, you must do this in place with constant memory.
 For example,
 Given input array A = [1,1,2],
 Your function should return length = 2, and A is now [1,2].

 Solution: Update 7/16/2013: Let j start from 0 for better understanding.
 """

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums == []: return 0
        i =  0
        for j in xrange(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1