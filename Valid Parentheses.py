"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 6, 2015
 Problem:    Valid Parentheses
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_20
 Notes:
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

 Solution: stack.
 """


class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        pairOfParentheses = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for char in s:
            if char in pairOfParentheses:
                stack.append(char)
            elif stack == [] or char != pairOfParentheses[stack.pop()]:
                return False
        return stack == []