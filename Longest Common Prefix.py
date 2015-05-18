"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 18, 2015
 Problem:    Longest Common Prefix
 Difficulty: Easy
 Source:     https://oj.leetcode.com/problems/longest-common-prefix/
 Notes:
 Write a function to find the longest common prefix string amongst an array of strings.

 Solution: ...
 """

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if strs == []: return ""
        prefix = strs[0]
        for str in strs[1:]:
            j, maxLength = 0, min(len(prefix), len(str))
            while j < maxLength and prefix[j] == str[j]:
                j += 1                
            prefix = prefix[:j]
        return prefix