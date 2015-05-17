"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 17, 2015
 Problem:    Count and Say
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_38
 Notes:
 The count-and-say sequence is the sequence of integers beginning as follows:
 1, 11, 21, 1211, 111221, ...

 1 is read off as "one 1" or 11.
 11 is read off as "two 1s" or 21.
 21 is read off as "one 2, then one 1" or 1211.
 Given an integer n, generate the nth sequence.
 Note: The sequence of integers will be represented as a string.

 Solution: ...
"""

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n == 1: return '1'
        s = self.countAndSay(n - 1)
        result, i = '', 0
        while i < len(s):
            j = 1
            while i < len(s) - 1 and s[i + 1] == s[i]: 
                i, j = i + 1, j + 1
            result += "{0}{1}".format(j, s[i])
            i += 1
        return result