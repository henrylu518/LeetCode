"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 16, 2015
 Problem:    Construct Binary Tree from Inorder and Postorder Traversal
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_106
 Notes:
 Given inorder and postorder traversal of a tree, construct the binary tree.
 Note:
 You may assume that duplicates do not exist in the tree.

 Solution: Recursion.
         using dictionary for index lookup improves the performance of algorithm from O(N^2) to O(N)

 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):

        lookup = {value : i for (i, value) in enumerate(inorder)}
        
        def buildTreeRecur(inStart, inEnd, postLast):
            if inStart > inEnd : return None
            i = lookup[postorder[postLast]]
            root = TreeNode(inorder[i])
            root.left = buildTreeRecur(inStart, i - 1, postLast - (inEnd - i + 1))
            root.right = buildTreeRecur(i + 1, inEnd, postLast - 1)
            return root
            
        return buildTreeRecur(0, len(inorder) - 1, len(postorder) - 1)
        