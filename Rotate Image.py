"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Rotate Image
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_48
 Notes:
 You are given an n x n 2D matrix representing an image.
 Rotate the image by 90 degrees (clockwise).
 Follow up:
 Could you do this in-place?

 Solution: 1. Rotate one-fourth of the image clockwise.
           2. 123   ->   963 ->  741    (preferable)
              456        852     852
              789        741     963
 """

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n - 1):
            for m in xrange(n - 1 - i):
                matrix[i][m], matrix[n - 1 - m][n - 1 - i] =  \
                matrix[n - 1 - m][n - 1 - i], matrix[i][m]
        for i in xrange(n):
            k, l = 0, n - 1
            while k < l:
                matrix[k][i], matrix[l][i] = matrix[l][i], matrix[k][i]
                k, l = k + 1, l - 1