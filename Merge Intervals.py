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
        if intervals == []: return []
        intervals = sorted(intervals, key = lambda m : m.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if result[-1].end >= intervals[i].start:
                result[-1].end = max(result[-1].end, intervals[i].end)
            else:
                result.append(intervals[i])
        return result