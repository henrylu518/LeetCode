"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Set Matrix Zeroes
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_73
 Notes:
 Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
 Follow up:

 Solution: 1. This solution use O(m + n) space. 
           2. use the first row and col to store the zero rows and cols. (constant space)

"""


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes_1(self, matrix):
        rows, cols = set(), set()
        for (i, row) in enumerate(matrix):
            for(j, value) in enumerate(row):
                if value == 0:
                    rows.add(i)
                    cols.add(j)
        colLength = len(matrix[0]) if matrix else 0
        rowLength = len(matrix)
        for i in rows:
            matrix[i] = [0] * colLength
        for j in cols:
            for i in xrange(rowLength):
                matrix[i][j] = 0

    def setZeros_2(self, matrix):
        if not matrix : return
        isZeroInFirstRow = False
        isZeroInFirstCol = False
        rowLength = len(matrix)
        colLength = len(matrix[0])

        for v in matrix[0]:
            if v == 0:
                isZeroInFirstRow = True
                break
        for i in xrange(rowLength):
            if matrix[i][0] == 0:
                isZeroInFirstCol = True


        for (i, row) in enumerate(matrix[1:], 1):
            for(j, value) in enumerate(row[1:], 1):
                if value == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in xrange(1, rowLength):
            if matrix[i][0] == 0:
                matrix[i] = [0] * colLength

        for j in xrange(1, colLength):
            if matrix[0][j] == 0:
                for i in xrange(rowLength):
                    matrix[i][j] = 0

        if isZeroInFirstRow:
            matrix[0] = [0] * colLength
        if isZeroInFirstCol:
            for i in xrange(rowLength):
                matrix[i][0] = 0


