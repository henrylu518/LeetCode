"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Valid Palindrome
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_125
 Notes:
 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 For example,
 "A man, a plan, a canal: Panama" is a palindrome.
 "race a car" is not a palindrome.
 Note:
 Have you consider that the string might be empty? This is a good question to ask during an interview.
 For the purpose of this problem, we define empty string as valid palindrome.

 Solution: traverse from both side.
 """

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while j > i:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1  
        return True
