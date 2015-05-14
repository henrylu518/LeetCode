"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Sum Root to Leaf Numbers
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_129
 Notes:
 Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
 An example is the root-to-leaf path 1->2->3 which represents the number 123.
 Find the total sum of all root-to-leaf numbers.
 For example,
   1
  / \
 2   3
 The root-to-leaf path 1->2 represents the number 12.
 The root-to-leaf path 1->3 represents the number 13.
 Return the sum = 12 + 13 = 25.

 Solution: 1. Recursion (add to sum when reaching the leaf).
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        
        def sumNumbersRecur(currentSum, node):
            if node == None:    return 0
            currentVal = currentSum * 10 + node.val
            if node.left == None and node.right == None: 
                return currentVal
            else:
                return sumNumbersRecur(currentVal, node.left) + sumNumbersRecur(currentVal, node.right)
        
        return sumNumbersRecur(0, root)


