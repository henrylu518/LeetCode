# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        
        def generateTreesRecur(nums):
            if nums == []: return [None]
            result = []
            for (i, num) in enumerate(nums):
                for leftRoot in generateTreesRecur(nums[:i]):
                    for rightRoot in generateTreesRecur(nums[i + 1:]):
                        root = TreeNode(num)
                        root.right = rightRoot
                        root.left = leftRoot
                        result.append(root)
            return result
            
        return generateTreesRecur(list(range(1, n + 1)))


    def generateTrees(self, n):
        
        def generateTreesRecur_Wrong(nums):
            """
                The root are the same root. Not only the value, but the 
                exactly node.
            """
            if nums == []: return [None]
            result = []
            for (i, num) in enumerate(nums):
                root = TreeNode(num)
                for leftRoot in generateTreesRecur(nums[:i]):
                    root.left = leftRoot
                    for rightRoot in generateTreesRecur(nums[i + 1:]):
                        root.right = rightRoot
                        result.append(root)
            return result
            
        return generateTreesRecur(list(range(1, n + 1)))