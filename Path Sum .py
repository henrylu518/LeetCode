"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 16, 2015
 Problem:    Path Sum
 Difficulty: easy
 Source:     http://www.leetcode.com/onlinejudge
 Notes:
 Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up 
 all the values along the path equals the given sum.

 For example:
 Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
 return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
 
 Solution: Recursion.
        (tree leaf: always to remember to check root.left and root.right to end recurse)
            
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        
        def hasPathSumRecur(currentSum, currentRoot):
            # currentRoot is never None
            currentSum += currentRoot.val
            if  currentRoot.left == None and currentRoot.right == None:
                return currentSum == sum
            result = False
            if currentRoot.right:
                result = hasPathSumRecur(currentSum, currentRoot.right)
            if currentRoot.left:
                result = result or hasPathSumRecur(currentSum, currentRoot.left)
            return result
            
        if root == None: return False
        return hasPathSumRecur(0, root)
        

    def hasPathSum_2(self, root, sum):
        if root == None: return False
        if root.right == None and root.left == None:
            return root.val == sum
        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)
        

        