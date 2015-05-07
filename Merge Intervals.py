"""
 Author:     Henry, henrylu@gmail.com
 Date:       May 7, 2015
 Problem:    Merge Intervals
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_56
 Notes:
 Given a collection of intervals, merge all overlapping intervals.
 For example,
 Given [1,3],[2,6],[8,10],[15,18],
 return [1,6],[8,10],[15,18].

 Solution: 1. Sort in ascending order of 'start'.
           2. When two intervals have overlapping area, merge them.
                while i < len(intervals) - 1: this will be much slower
                We could track the intervalsLength by ourself. When there is a merge,
                then decrease the intervalsLength

"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda m : m.start)
        i = 0
        intervalsLength = len(intervals)
        while i < intervalsLength - 1:
            if intervals[i + 1].start <= intervals[i].end:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                intervals.pop(i + 1)
                intervalsLength -= 1
            else:
                i += 1
        return intervals