"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Binary Tree Zigzag Level Order Traversal
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_103
 Notes:
 Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left 
 to right, then right to left for the next level and alternate between).
 For example:
 Given binary tree {3,9,20,#,#,15,7},
     3
    / \
   9  20
  / \
 15  7
 return its zigzag level order traversal as:
 [
  [3],
  [20,9],
  [15,7]
 ]

 Solution: 
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root: return []
        leftToRight, currentLevelNodes, result = True, [root], []
        while currentLevelNodes:
            nextLevelNodes, currentLevelVal = [], []
            while currentLevelNodes:
                node = currentLevelNodes.pop()
                currentLevelVal.append(node.val)
                if leftToRight:
                    if node.left: nextLevelNodes.append(node.left)
                    if node.right: nextLevelNodes.append(node.right)
                else:
                    if node.right: nextLevelNodes.append(node.right)
                    if node.left: nextLevelNodes.append(node.left)
            result.append(currentLevelVal)
            currentLevelNodes = nextLevelNodes
            leftToRight = not leftToRight
        return result
                
            