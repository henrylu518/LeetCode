"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 14, 2015
 Problem:    Partition List
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_86
 Notes:
 Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
 You should preserve the original relative order of the nodes in each of the two partitions.
 For example,
 Given 1->4->3->2->5->2 and x = 3,
 return 1->2->2->4->3->5.

 Solution: Remember to set right.next = None, or the list will have a loop.
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        dummyLeft, dummyRight = ListNode(None), ListNode(None)
        left, right = dummyLeft, dummyRight
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = dummyRight.next
        return dummyLeft.next