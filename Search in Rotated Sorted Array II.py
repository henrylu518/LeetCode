"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 24, 2015
 Problem:    Search in Rotated Sorted Array II
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_81
 Notes:
 Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 What if duplicates are allowed?
 Would this affect the run-time complexity? How and why?
 Write a function to determine if a given target is in the array.

 Solution: Sequence search. O(n)
           Since there are duplicates, it's hard to decide left or right is sorted.
           For example: [1,1,3,1] nums[middle] == nums[low], nums[middle] == nums[high]
           Once there is diffience between nums[middle], nums[low], nums[high],
           we can know which branch is sorted, and then decide which branch to search next.
 """

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low + high) / 2
            if nums[middle] == target:
                return True
            while nums[middle] == nums[low] and nums[middle] == nums[high] and high > low:
                low += 1
                high -= 1
            if (nums[middle] >= nums[low] and target >= nums[low] and target < nums[middle]) or \
            (nums[middle] <= nums[high] and (target < nums[middle] or target > nums[high])):
                high = middle - 1
            else:
                low = middle + 1
        return False

