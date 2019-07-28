"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if newInterval.end < interval.start:
                results.append(interval)
            elif interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)

        results.insert(insertPos, newInterval)
        return results
