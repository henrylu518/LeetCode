class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
    	if obstacleGrid[-1][-1] == 1: return 0
    	m, n = len(obstacleGrid), len(obstacleGrid[0])
        table = [[0 for _ in range(n)] for _ in range(m)]
        table[-1][-1] = 1
        for i in xrange(m - 1, -1, -1):
        	for j in xrange(n - 1, -1, -1):
        		if obstacleGrid[i][j] == 0: 
        			if i < m - 1:
        				table[i][j] += table[i + 1][j]
        			if j < n - 1:
        				table[i][j] += table[i][j + 1]
        return table[0][0]

