class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if height == []: return 0
        leftMax, rightMax = [0] * len(height), [0] * len(height)
        leftMax[0], rightMax[len(height) - 1]  = height[0], height[len(height) - 1]
        for i in xrange(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])
        for i in xrange(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        trapped = 0
        for i in xrange(len(height)):
            trapped += min(leftMax[i], rightMax[i]) - height[i]
        return trapped