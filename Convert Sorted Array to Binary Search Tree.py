"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 15, 2015
 Problem:    Convert Sorted Array to Binary Search Tree
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_108
 Notes:
 Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

 Solution: Recursion. (use index to pass the parameter, instead of the entire subarray. save space)
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        def sortedArrayToBST(start, end):
            if start > end: return None
            middle = (start + end) / 2
            root = TreeNode(nums[middle])
            root.left = sortedArrayToBST(start, middle - 1)
            root.right = sortedArrayToBST(middle + 1, end)
            return root

        return sortedArrayToBST(0, len(nums) - 1)
            
        