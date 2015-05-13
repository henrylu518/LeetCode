"""
 Author:     Henry, henrylu@gmail.com
 Date:       May 9, 2015
 Problem:    Roman to Integer
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_13
 Notes:
 Given a roman numeral, convert it to an integer.
 Input is guaranteed to be within the range from 1 to 3999.

 Solution: use map (clean)
 """

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        table = {"M": 1000, "D": 500, "C":100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        sLen = len(s)
        for i in xrange(sLen):
            if i + 1 < sLen and table[s[i + 1]] > table[s[i]]:
                result -= table[s[i]]
            else:
                result += table[s[i]]
        return result