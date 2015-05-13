"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 13, 2015
 Problem:    Merge k Sorted Lists
 Difficulty: easy
 Source:     http://leetcode.com/onlinejudge#question_23
 Notes:
 Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
 
 Solution: 
    1. Simple Solution, complexity: O(nklog(nk))
    2. Use heap to find minimum value, complexity: O(nklog(k))
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists_1(self, lists):
        n, i, result = len(lists), 0, []
        while i < n:
            while lists[i] != None:
                result.append(lists[i].val)
                lists[i] = lists[i].next
            i += 1
        return sorted(result)

    def mergeKLists_2(self, lists):
        result, heap = [], []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l.next))
        while heap:
            value, nextNode = heapq.heappop(heap)
            result.append(value)
            if nextNode:
                heapq.heappush(heap, (nextNode.val, nextNode.next))
        return result

        