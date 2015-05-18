"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Spiral Matrix II
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_59
 Notes:
 Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
 For example,
 Given n = 3,
 You should return the following matrix:
 [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
 ]

 Solution: ...
 """

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        rowStart, rowEnd, colStart, colEnd = 0, n - 1, 0, n - 1
        num = 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in xrange(colStart, colEnd + 1):
                matrix[rowStart][i] = num
                num += 1
            for i in xrange(rowStart + 1, rowEnd):
                matrix[i][colEnd] = num
                num += 1
            if rowStart != rowEnd:
                for i in xrange(colEnd, colStart - 1, -1):
                    matrix[rowEnd][i] = num
                    num += 1
                for i in xrange(rowEnd - 1, rowStart, - 1):
                    matrix[i][colStart] = num
                    num += 1
            rowStart += 1; rowEnd -= 1
            colStart += 1; colEnd -= 1
        return matrix