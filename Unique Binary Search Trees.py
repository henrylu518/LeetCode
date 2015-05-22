class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n < 0: return 0
        if n == 0: return 1
        ways = {0: 1}
        for i in xrange(1, n + 1):
            way = 0
            for j in xrange(i):
                way += ways.get(j, 1) * ways.get(i - j - 1, 1)
            ways[i] = way
        return ways[n]