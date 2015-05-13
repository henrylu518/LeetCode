"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 13, 2015
 Problem:    Minimum Path Sum
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_64
 Notes:
 Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right 
 which minimizes the sum of all numbers along its path.
 Note: You can only move either down or right at any point in time.

 Solution: Dynamic Programming. 
            1. Naive Solution,  Space O(N^2).
            2. Space O(N).
            3. Space O(1), but modified the grid.

 """

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        table = [[None for _ in range(n)] for _ in range(m)]
        table[-1][-1] = grid[-1][-1]
        for i in xrange(m - 1, -1, -1 ):
        	for j in xrange(n - 1, -1, -1):
        		if i < m - 1 and j < n - 1:
        			table[i][j] = grid[i][j] + min(table[i + 1][j], table[i][j + 1])
        		elif i == m - 1 and j != n - 1:
        			table[i][j] = grid[i][j] + table[i][j + 1]
        		elif j == n - 1 and i != m - 1:
        			table[i][j] = grid[i][j] + table[i + 1][j]
        return table[0][0]

    def minPathSum_2(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for j in xrange(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in xrange(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in xrange(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]

    def minPathSum_3(self, grid):
        m, n = len(grid), len(grid[0])
        for j in xrange(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in xrange(1, m):
            grid[i][0] += grid[i - 1][0]
            for j in xrange(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]) 
        return grid[m - 1][n - 1]