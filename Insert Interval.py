# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        intervalsLength = len(intervals)
        i = 0
        while intervals[i].end < newInterval.start: 
            i += 1
            if i >= intervalsLength:
                intervals.append(newInterval)
                return intervals
        newInterval.start = min(newInterval.start, intervals[i].start)
        intervals.insert(i, newInterval)
        intervalsLength += 1
        while i + 1 < intervalsLength:
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                intervals.pop(i + 1)
                intervalsLength -= 1
            else:
                return intervals
        return intervals