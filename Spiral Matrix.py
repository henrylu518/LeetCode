"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Spiral Matrix
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_54
 Notes:
 Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 For example,
 Given the following matrix:
 [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
 ]
 You should return [1,2,3,6,9,8,7,4,5].

 Solution: ...
 """

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        
        def spiralOrderRecur(rowStart, rowEnd, colStart, colEnd):
            if rowStart > rowEnd or colStart > colEnd:
                return []
            outside = matrix[rowStart][colStart: colEnd + 1]
            for i in xrange(rowStart + 1, rowEnd):
                outside.append(matrix[i][colEnd])
            if rowEnd != rowStart:
                outside += list(reversed(matrix[rowEnd][colStart: colEnd + 1]))
            if colEnd != colStart:
                for i in xrange(rowEnd - 1, rowStart, -1):
                    outside.append(matrix[i][colStart])
            return outside + spiralOrderRecur(rowStart + 1, rowEnd - 1, colStart + 1, colEnd - 1)
            
        if matrix == []: return []     
        row, col = len(matrix), len(matrix[0])
        return spiralOrderRecur(0, row - 1, 0, col - 1)

    def spiralOrder_2(self, matrix):
        result = []
        if matrix == [] or matrix[0] == []:
            return result
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return result