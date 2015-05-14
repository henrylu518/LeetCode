"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Binary Tree Inorder Traversal
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_94
 Notes:
 Given a binary tree, return the inorder traversal of its nodes' values.
 For example:
 Given binary tree {1,#,2,3},
 1
  \
   2
  /
 3
 return [1,3,2].
 Note: Recursive solution is trivial, could you do it iteratively?

 Solution: 1. Iterative way (stack).   Time: O(n), Space: O(n).
           2. Recursive solution.      Time: O(n), Space: O(n).
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        def inorderTraversalRecur(result, node):
            if node == None: return
            inorderTraversalRecur(result, node.left)
            result.append(node.val)
            inorderTraversalRecur(result, node.right)
            
        result = []
        inorderTraversalRecur(result, root)
        return result

    def inorderTraversal_2(self, root):
        stack, current = [], root
        result = []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                result.append(node.val)
                current = node.right
        return result