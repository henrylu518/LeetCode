"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Valid Sudoku
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_36
 Notes:
 Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules (http://sudoku.com.au/TheRules.aspx).
 The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

 Solution:  Traverse the Sudoku.
 """

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if len(board) != 9 or len(board[0]) != 9: 
            return False
        for row in board:
            rowNums = set()
            for num in row:
                if num != '.':
                    if num in rowNums: return False
                    rowNums.add(num)
        for j in xrange(9):
            colNums = set()
            for i in xrange(9):
                num = board[i][j]
                if num != '.':
                    if num in colNums: return False
                    colNums.add(num)
        for rowStart in [0, 3, 6]:
            for colStart in [0, 3, 6]:
                squareNums = set()
                for i in xrange(rowStart, rowStart + 3):
                    for j in xrange(colStart, colStart + 3):
                        num = board[i][j]
                        if num != '.':
                            if num in squareNums: return False
                            squareNums.add(num)
        return True


    
    def isValidList(self, l):
        l = filter(lambda x: x != '.', l)
        return len(set(l)) == len(l)
    
    def isValidSudoku_2(self, board):
        if len(board) != 9 or len(board[0]) != 9:
            return False
        for i in xrange(9):
            if not self.isValidList(board[i]) or not self.isValidList(board[j][i] for j in range(9)):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not self.isValidList([board[m][n] for m in xrange(i, i + 3) for n in xrange(j, j + 3)]):
                    return False
        return True

        