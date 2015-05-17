"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 17, 2015
 Problem:    Next Permutation
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_31
 Notes:
 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
 If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
 The replacement must be in-place, do not allocate extra memory.
 Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
 1,2,3 -> 1,3,2
 3,2,1 -> 1,2,3
 1,1,5 -> 1,5,1

 Solution: O(n)
 Processes: 
 """

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0 :
            nums.reverse()
            return 
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = list(reversed(nums[i:]))
        return 
        