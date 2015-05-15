# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def findMedian(self, head):
        one, two, previous = head, head, None
        while two and two.next and two.next.next:
            previous = one
            one = one.next
            two = two.next.next
        return previous, one
    
    def sortedListToBST(self, head):
        if head == None: return head
        previous, median = self.findMedian(head)
        root = TreeNode(median.val)
        if previous: 
            previous.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(median.next)
        return root
        