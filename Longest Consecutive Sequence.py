"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Longest Consecutive Sequence
 Difficulty: Hard
 Source:     https://oj.leetcode.com/problems/longest-consecutive-sequence/
 Notes:
 Given an unsorted array of integers, find the length of the longest consecutive 
 elements sequence.
 For example,
 Given [100, 4, 200, 1, 3, 2],
 The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
 Your algorithm should run in O(n) complexity.

 Solution 1: use a set or a dict
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        numsSet, longest = set(nums), 0
        for num in nums:
            length = 1
            if num in numsSet:
                numsSet.remove(num)
                left, right = num - 1, num + 1
                while right in numsSet:
                    numsSet.remove(right)
                    right += 1
                    length += 1
                while left in numsSet:
                    numsSet.remove(left)
                    left -= 1
                    length += 1
            longest = max(longest, length)
        return longest

    def longestConsecutive_2(self, nums):
        numsDict = {num : False for num in nums}
        longest = 0
        for num in nums:
            length = 1
            if numsDict[num] == False:
                numsDict[num] = True
                left, right = num - 1, num + 1
                while left in numsDict:
                    numsDict[left] = True
                    left -= 1
                    length += 1
                while right in numsDict:
                    numsDict[right] = True
                    right += 1
                    length += 1
            longest = max(longest, length)
        return longest



