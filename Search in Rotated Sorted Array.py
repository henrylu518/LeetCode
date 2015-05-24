"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 24, 2015
 Problem:    Search in Rotated Sorted Array
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_33
 Notes:
 Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 You are given a target value to search. If found in the array return its index, otherwise return -1.
 You may assume no duplicate exists in the array.

 Solution: Binary search. O(log(n)) check middle, either start to middle is sorted or middle to end is sorted, 
            use the sorted nums to check whether left or right to search
 """

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (high + low) / 2
            if nums[middle] == target:
                return middle
            elif (nums[0] < nums[middle] and target >= nums[0] and target < nums[middle]) \
            or (nums[middle] < nums[high] and (target < nums[middle] or target > nums[high])):
                high = middle - 1
            else:
                low = middle + 1
        return -1

    