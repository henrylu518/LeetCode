"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 16, 2015
 Problem:    Flatten Binary Tree to Linked List
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_114
 Notes:
 Given a binary tree, flatten it to a linked list in-place.
 For example,
 Given
     1
    / \
   2   5
  / \   \
 3   4   6
 The flattened tree should look like:
 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
 Hints:
 If you notice carefully in the flattened tree, each node's right child points to the next node
 of a pre-order traversal.

 Solution: Recursion. Return the last element of the flattened sub-tree.
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    
    last = None
    
    def flatten(self, root):
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.last
            root.left = None
            self.last = root

    def flatten_2(self, root):
        def flattenRecur(root):
            if root == None: return None
            left = root.left
            right = root.right
            root.left, root.right = None, None
            if left:
                root.right = flattenRecur(left)
            newRightRoot = flattenRecur(right)
            current = root
            while current.right:
                current = current.right
            current.right = newRightRoot
            return root
        flattenRecur(root)
        
            