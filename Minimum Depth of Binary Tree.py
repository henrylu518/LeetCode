# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root == None: return 0
        current, depth = [root], 1
        while True:
            next = []
            for node in current:
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current, depth = next, depth + 1