class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        table = [[ 0 ] * n] * m
        table[m - 1] = [1] * n
        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 1, -1, -1):
                table[i][j] = table[i + 1][j]
                if j < n - 1:
                    table[i][j] += table[i][j + 1]
        return table[0][0]

    def uniquePaths_Wrong(self, m, n):
        """
            This line is the trouble: table[i][j] += table[i + 1][j].

        """
        table = [[ 0 ] * n] * m
        table[m - 1] = [1] * n
        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 1, -1, -1):
                table[i][j] += table[i + 1][j]
                if j < n - 1:
                    table[i][j] += table[i][j + 1]
        return table[0][0]

    def uniquePaths_2(self, m, n):
        """
            use the finish as the [0,0]
        """
        table = [[1] for _ in range(m)]
        for _ in xrange(n - 1):
            table[0].append(1)
        for i in xrange(1, m):
            for j in xrange(1, n):
                table[i].append(table[i - 1][j] + table[i][j - 1])
        return table[m - 1][n - 1]


