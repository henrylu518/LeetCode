"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 9, 2015
 Problem:    Generate Parentheses
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_22
 Notes:
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 For example, given n = 3, a solution set is:
 "((()))", "(()())", "(())()", "()(())", "()()()"

 Solution: Place n left '(' and n right ')'.
           Cannot place ')' if there are no enough matching '('.

           1. iterative
           2. recursive
 """

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis_1(self, n):
        result = [("", 0, 0)]
        for _ in xrange(2 * n):
        	current = []
        	for s, leftCount, rightCount in result:
        		if leftCount < n:
        			current.append((s + "(", leftCount + 1, rightCount))
        		if leftCount - rightCount > 0 :
        			current.append((s + ")", leftCount, rightCount + 1))
        	result = current
        return [parenthesis for (parenthesis, leftCount, rightCount) in result]

    def generateParenthesis_2(self, n):
    	def generateParenthesisBasedOn(result, current, left, right):
    		if left == 0 and right == 0:   result.append(current)
    		if left > 0: generateParenthesisBasedOn(result, current + "(", left - 1, right)
    		if right > left: generateParenthesisBasedOn(result, current + ")", left, right - 1)
    	result = []
    	generateParenthesisBasedOn(result, "", n, n)
    	return result

