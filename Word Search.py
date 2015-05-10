

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if board == [[]]: return False
        m, n, k = len(board), len(board[0]), len(word)
        
        def successorPosition(i, j):
            candidate = [[i + 1, j], [i - 1, j], [i, j + 1],[i, j - 1]]
            position = [p for p in candidate 
                    if p[0] >= 0 and p[0] < m and p[1] >= 0 and p[1] < n]
            return position
        
        def startFrom(i, j, visited, matchedPosition):
            matchedPosition += 1
            if board[i][j] != word[matchedPosition] or visited[i][j] == 1: return False
            if matchedPosition == k - 1: return True
            visited[i][j] = 1
            for (i1, j1) in successorPosition(i,j):
                if startFrom(i1, j1, visited, matchedPosition):
                    return True
            visited[i][j] = 0
            return False
        
        visited = [[0 for y in range(len(board[0]))] for x in range(len(board))]
        for i in xrange(m):
            for j in xrange(n):
                if startFrom(i,j, visited, -1):
                    return True
        return False
