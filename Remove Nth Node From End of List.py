"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Remove Nth Node From End of List
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_19
 Notes:
 Given a linked list, remove the nth node from the end of list and return its head.
 For example,
 Given linked list: 1->2->3->4->5, and n = 2.
 After removing the second node from the end, the linked list becomes 1->2->3->5.
 Note:
 Given n will always be valid.
 Try to do this in one pass.

 Solution: head---back------front------>NULL
                   |          |
                   ---> n <----
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, head
        while n:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        