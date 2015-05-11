# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):	
        if root == None: return []
        currentLevel = [root]
        result = []
        while currentLevel:
            currentVal = [e.val for e in currentLevel]
            result.append(currentVal)
            nextLevel = []
            for node in currentLevel:
            	if node.left:
                	nextLevel.append(node.left) 
                if node.right:
                	nextLevel.append(node.right) 
            currentLevel = nextLevel
        return result
        