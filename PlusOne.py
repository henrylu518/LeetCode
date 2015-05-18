"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Plus One
 Difficulty: Easy
 Source:     https://oj.leetcode.com/problems/plus-one/
 Notes:
 Given a number represented as an array of digits, plus one to the number.

 Solution: ...
 """

 class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if digits == []: return []
        carry, i = 1, len(digits) - 1
        while carry and i >= 0:
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum / 10
            i -= 1
        if carry: digits.insert(0, 1)
        return digits
        
        