"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 9, 2015
 Problem:    Anagrams
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_49
 Notes:
 Given an array of strings, return all groups of strings that are anagrams.
 Note: All inputs will be in lower-case.

 Solution: Sort the string to see if they're anagrams.
 """

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        table = {}
        for str in strs:
            key = "".join(sorted(str))
            table[key] = table.get(key, []) + [str]
        result = []
        for strs in table.values():
            if len(strs) > 1:
                result += strs
        return result