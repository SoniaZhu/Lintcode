"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result

## mine
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        res = []
        intervals.sort(key = lambda x : x.start)
        for i in range(len(intervals)):
            if i == len(intervals) - 1 or intervals[i].end < intervals[i + 1].start:
                res.append(intervals[i])
            else:
                intervals[i + 1].start = intervals[i].start
                intervals[i + 1].end = max(intervals[i].end, intervals[i + 1].end)
        return res
