"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Decode Ways
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_91
 Notes:
 A message containing letters from A-Z is being encoded to numbers using the following mapping:
 'A' -> 1
 'B' -> 2
 ...
 'Z' -> 26
 Given an encoded message containing digits, determine the total number of ways to decode it.
 For example,
 Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
 The number of ways decoding "12" is 2.

 Solution: 1. dp. Time : O(n); Space : O(1). 
            (just be careful of '0' and the initial state of prev and prev_prev)
 """

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        current, prev, prev_prev = 0, 1, 1
        s = s[::-1]
        for i in xrange(len(s)):
            if s[i] == '0':
                current = 0
            else:
                if i > 0 and (s[i] == '1' 
                  or (s[i] == '2' and int(s[i - 1]) <= 6)):
                    current = prev + prev_prev
                else:
                    current = prev
            prev, prev_prev = current, prev
        return current