"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 17, 2015
 Problem:    Reverse Nodes in k-Group
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_25
 Notes:
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
 You may not alter the values in the nodes, only nodes itself may be changed.
 Only constant memory is allowed.
 For example,
 Given this linked list: 1->2->3->4->5
 For k = 2, you should return: 2->1->4->3->5
 For k = 3, you should return: 3->2->1->4->5

 Solution: 1. recursive (not constant memory)
           2. iterative (constant memory)
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if k <= 1: return head
        current, i = head, 0
        while current and i < k:
            current = current.next
            i += 1
        if i < k: return head
        dummy, i = ListNode(None), 0
        dummy.next = self.reverseKGroup(current, k)
        current = head
        while i < k:
            nextNode = current.next
            current.next = dummy.next
            dummy.next = current
            current = nextNode
            i += 1
        return dummy.next




    def getLength(self, head):
        i = 0
        while head:
            i += 1
            head = head.next
        return i
    
    def reverseKGroup_2(self, head, k):
        if k <= 1: return head
        reverseTime = self.getLength(head) / k
        if reverseTime == 0: return head
        dummy = ListNode(None)
        dummy.next = None
        previous, current = dummy, head
        for _ in xrange(reverseTime):
            first = current
            for _ in xrange(k):
                nextNode = current.next
                current.next = previous.next
                previous.next = current
                current = nextNode
            previous = first
        previous.next = current
        return dummy.next
        