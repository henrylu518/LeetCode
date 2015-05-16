"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 16, 2015
 Problem:    Longest Substring Without Repeating Characters
 Difficulty: Medium
 Source:     https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
 Notes:
 Given a string, find the length of the longest substring without repeating characters. 
 For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
 For "bbbbb" the longest substring is "b", with the length of 1.

 Solution: 
 """
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        longest, start, lookUp = 0, 0,  {}
        for (i, c) in enumerate(s):
            if c in lookUp:
                position = lookUp[c]
                for j in xrange(start, position + 1):
                    del lookUp[s[j]]
                start = position + 1
            lookUp[c] = i
            longest = max(longest, i - start + 1)
        return longest


    def lengthOfLongestSubstring_2(self, s):
        visited, longest, start = [False for _ in range(256)], 0, 0
        for (i, c) in enumerate(s):
            if visited[ord(c)]:
                while s[start] != c:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            visited[ord(c)] = True
            longest = max(longest, i - start + 1)
        return longest