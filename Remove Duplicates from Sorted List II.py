"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Remove Duplicates from Sorted List II
 Difficulty: Easy
 Source:     https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
 Notes:
 Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
 For example,
 Given 1->2->3->3->4->4->5, return 1->2->5.
 Given 1->1->1->2->3, return 2->3.

 Solution: iterative 
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy = ListNode(None)
        dummy.next = head
        previous = dummy
        while head:
            while head and head.next and head.val == head.next.val:
                value = head.val
                while head and head.val == value:
                    head = head.next
            previous.next = head
            previous = previous.next
            if head: head = head.next
        return dummy.next  