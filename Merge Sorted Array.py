"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Merge Sorted Array
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_88
 Notes:
 Given two sorted integer arrays A and B, merge B into A as one sorted array.
 Note:
 You may assume that A has enough space to hold additional elements from B. 
 The number of elements initialized in A and B are m and n respectively.

 Solution: Backward.
 """

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i] 
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1    