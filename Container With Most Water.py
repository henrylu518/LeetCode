"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 16, 2015
 Problem:    Container With Most Water
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_11
 Notes:
 Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.
 Note: You may not slant the container.

 Solution: From both sides to the center.
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        i, j, mArea = 0, len(height) - 1, 0
        while i < j:
            mArea = max(mArea, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mArea