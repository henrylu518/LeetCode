"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Implement strStr()
 Difficulty: Easy
 Source:     https://oj.leetcode.com/problems/implement-strstr/
 Notes:
 Implement strStr().
 Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.

 """

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        for i in xrange(0, len(haystack) - len(needle) + 1):
            if haystack[i: i + needleLength] == needle:
                return i
        return -1