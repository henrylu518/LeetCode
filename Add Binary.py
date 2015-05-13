"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 10, 2015
 Problem:    Add Binary
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_67
 Notes:
 Given two binary strings, return their sum (also a binary string).
 For example,
 a = "11"
 b = "1"
 Return "100".

 Solution
 """

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary_1(self, a, b):
        i, j, carry = len(a) - 1, len(b) - 1, 0
        result = ""
        while i >= 0 or j >= 0:
            current = carry
            if i >= 0:
                current += int(a[i])
                i -= 1
            if j >= 0:
                current += int(b[j])
                j -= 1
            carry = current / 2
            current %= 2
            result = str(current) + result
        if carry: result = "1" + result
        return result

    def addBinary_2(self, a, b):
        """ Use build in functions """
        return bin(int(a, 2) + int(b, 2)).split('b')[1]

