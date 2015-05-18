"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Jump Game
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_55
 Notes:
 Given an array of non-negative integers, you are initially positioned at the first index of the array.
 Each element in the array represents your maximum jump length at that position.
 Determine if you are able to reach the last index.
 For example:
 A = [2,3,1,1,4], return true.
 A = [3,2,1,0,4], return false.

 Solution: 
 """

class Solution:
    # @param {integer[]} nums
    # @return {boolean}

    def canJump(self, nums):
        reachable = 0
        for i in xrange(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True

    def canJump_2(self, nums):
        i, reachable = 0, 0
        while reachable < len(nums) - 1:
            nextReachable = reachable
            while i <= reachable:
                nextReachable = max(nextReachable, nums[i] + i)
                i += 1
            if nextReachable == reachable:
                return False
            reachable = nextReachable
        return True