"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Add Two Numbers
 Difficulty: easy
 Source:     http://www.leetcode.com/onlinejudge
 Notes:
 You are given two linked lists representing two non-negative numbers. 
 The digits are stored in reverse order and each of their nodes contain a single digit. 
 Add the two numbers and return it as a linked list.

 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8

 Solution: dummy head...

 """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers_1(self, l1, l2):
        def listToNumber(l):
            number = 0
            order = 0
            while l:
                number += l.val * 10 ** order
                order += 1
                l = l.next
            return number
            
        def numberToList(num):
            if num == 0: return ListNode(0)
            head = ListNode(0)
            prev = head
            while num:
                prev.next = ListNode(num % 10)
                num = num / 10
                prev = prev.next
            return head.next
            
        return numberToList(listToNumber(l1) + listToNumber(l2))

    def addTwoNumbers_2(self, l1, l2):
        carrier = 0 
        dummy = ListNode(0)
        prev = dummy
        while l1 or l2 or carrier:
            currentDigit = carrier
            if l1:
                currentDigit += l1.val
                l1 = l1.next
            if l2:
                currentDigit += l2.val
                l2 = l2.next
            if currentDigit > 9:
                carrier = 1
                currentDigit %= 10
            else:
                carrier = 0
            prev.next = ListNode(currentDigit)
            prev = prev.next
        return dummy.next

