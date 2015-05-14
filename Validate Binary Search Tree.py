

"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Validate Binary Search Tree
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_98
 Notes:
 Given a binary tree, determine if it is a valid binary search tree (BST).
 Assume a BST is defined as follows:
 The left subtree of a node contains only nodes with keys less than the node's key.
 The right subtree of a node contains only nodes with keys greater than the node's key.
 Both the left and right subtrees must also be binary search trees.

 Solution: 1. Recursion.  Add lowerBound and upperBound. O(n)
           2. inorder tree search           
 
 """


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        def isBSTInRange(root, lowerBound, upperBound):
            if not root: return True
            rootVal = root.val
            if rootVal <= lowerBound or rootVal >= upperBound:
                return False
            return isBSTInRange(root.left, lowerBound, rootVal) and \
                isBSTInRange(root.right, rootVal, upperBound)
        return isBSTInRange(root, -float("inf"), float("inf"))


    def isValidBST(self, root):
        def inorder(root, prev):
            if root == None: return True
            if not inorder(root.left, prev):
                return False
            if prev[0] and root.val <= prev[0].val:
                return False
            prev[0] = root
            return inorder(root.right, prev)
            
        prev = [None]
        return inorder(root, prev)
