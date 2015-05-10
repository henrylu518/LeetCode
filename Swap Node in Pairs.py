"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 9, 2015
 Problem:    Swap Nodes in Pairs
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_24
 Notes:
 Given a linked list, swap every two adjacent nodes and return its head.
 For example,
 Given 1->2->3->4, you should return the list as 2->1->4->3.
 Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

 Solution: 1. Iterative solution with constant space.
           2. Recursive solution with O(n) space (for practice).
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs_1(self, head):
        dummy = ListNode(0)
        dummy.next = head
        point, previousHead = head, dummy
        while point and point.next:
            second, third = point.next, point.next.next
            previousHead.next = second
            second.next = point
            point.next = third
            previousHead = point
            point = point.next
        return dummy.next
        
    def swapPairs_2(self, head):
        if head == None or head.next == None: return head
        third = head.next.next
        second = head.next
        second.next = head
        head.next = self.swapPairs(third)
        return second