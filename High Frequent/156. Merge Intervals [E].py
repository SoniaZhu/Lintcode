"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # # write your code here
        # intervals = sorted(intervals, key = lambda x : x.start)
        # result = []
        # i = 0
        # while i < len(intervals):
        #     start = intervals[i].start
        #     end = intervals[i].end
        #     i += 1
        #     while i < len(intervals) and intervals[i].start <= end:
        #         end = max(end, intervals[i].end)
        #         i += 1
        #     result.append(Interval(start, end))
        # return result


        intervals = sorted (intervals, key = lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
