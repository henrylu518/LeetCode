"""
 Date:       May 18, 2015
 Problem:    Jump Game II
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_45
 Notes:
 Given an array of non-negative integers, you are initially positioned at the first index of the array.
 Each element in the array represents your maximum jump length at that position.
 Your goal is to reach the last index in the minimum number of jumps.
 For example:
 Given array A = [2,3,1,1,4]
 The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

 Solution: Jump to the position where we can jump farthest (index + A[index]) next time.
 """

class Solution:
    # @param {integer[]} nums
    # @return {integer}

    def jump(self, nums):
        i, reachable, step = 0, 0, 0
        while reachable < len(nums) - 1:
            nextReachable = reachable
            while i <= reachable and i < len(nums):
                nextReachable = max(i + nums[i], nextReachable)
                i += 1
            reachable = nextReachable
            step += 1
        return step

    def jump_2(self, nums):
        if len(nums) in [0, 1]: return 0
        queue, visited = [(0, 0)], set()
        while queue:
            i,steps  = queue.pop(0)
            if i not in visited:
                visited.add(i)
                for j in xrange(nums[i], 0, -1):
                    if i + j >= len(nums) - 1:
                        return steps + 1
                    queue.append((i + j, steps + 1))


