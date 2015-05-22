"""
    TreeNode(1) != TreeNode(1)
    TreeNode(1).val == TreeNode(1).val
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
    def isSymmetric(self, root):
        if root == None: return True
        currentLeft= [root.left]
        currentRight = [root.right]
        while currentLeft or currentRight:
            if len(currentLeft) != len(currentRight):
                return False
            for i in xrange(len(currentLeft)):
                if currentLeft[i] and currentRight[-i - 1] and currentLeft[i].val != currentRight[-i - 1].val:
                    return False
                if (currentLeft[i] and currentRight[-i - 1] == None) or (currentLeft[i] == None and currentRight[-i - 1]):
                    return False
            nextLeft, nextRight = [], []
            for i in xrange(len(currentLeft)):
                if currentLeft[i]:
                    nextLeft += [currentLeft[i].left, currentLeft[i].right]
                if currentRight[i]:
                    nextRight += [currentRight[i].left, currentRight[i].right]
            currentLeft, currentRight = nextLeft, nextRight
        return True