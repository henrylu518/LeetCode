class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0: return []
        result = [[1]]
        for i in xrange(1, numRows):
            next = []
            for j in xrange(i + 1):
                if j == 0:
                    next.append(result[-1][0])
                elif j > 0 and j < i:
                    next.append(result[-1][j - 1] + result[-1][j])
                else:
                    next.append(result[-1][j - 1])
            result.append(next)
        return result