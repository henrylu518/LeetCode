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