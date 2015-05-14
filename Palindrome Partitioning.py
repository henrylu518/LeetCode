"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Palindrome Partitioning
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_131
 Notes:
 Given a string s, partition s such that every substring of the partition is a palindrome.
 Return all possible palindrome partitioning of s.
 For example, given s = "aab",
 Return
 [
  ["aa","b"],
  ["a","a","b"]
 ]

 Solution: ...
 """
        
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
        
    def partition(self, s):
        sLen = len(s)
        
        def partitionRecur(result, current, s, i):
            if i == sLen: 
                result.append(current)
            else:
                for j in xrange(i,sLen):
                    if self.isPalindrome(s[i:j + 1]):
                        partitionRecur(result, current + [s[i:j + 1]], s, j + 1)
        
        result = []
        partitionRecur(result, [], s, 0)
        return result

