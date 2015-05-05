__author__ = 'seany'

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # First sort the intervals according to their start;
        # intervals = self.sort(intervals, 0, len(intervals)-1)
        i = 0
        new_intervals = []
        if len(intervals) == 0:
            return new_intervals
        tmp = intervals[0]
        for i in xrange(1, len(intervals)):
            if tmp.end < intervals[i].start:
                new_intervals.append(tmp)
                tmp = intervals[i]
            else:
                if tmp.end < intervals[i].end:
                    tmp.end = intervals[i].end
        new_intervals.append(tmp)
        return new_intervals


    def sort(self, intervals, start, end):
        if start >= end - 1:
            if start == end:
                pass
            else:
                if intervals[start].start > intervals[end].start:
                    intervals[start], intervals[end] = intervals[end], intervals[start]
                else:
                    pass
        else:
            pivot = intervals[end].start
            i = start -1
            j = start
            # Here we will use quick sort to fix it!
        for i in xrange(length):
            pass


if __name__ == "__main__":
    intervals = []
    interval_1 = Interval(1, 3)
    interval_2 = Interval(4, 5)
    interval_3 = Interval(6, 9)
    interval_4 = Interval(8, 100)
    interval_5 = Interval(23, 901)
    intervals.append(interval_1)
    intervals.append(interval_2)
    intervals.append(interval_3)
    intervals.append(interval_4)
    intervals.append(interval_5)

    solution = Solution()
    new_intervals = solution.merge(intervals)
    for i in new_intervals:
        print i.start, i.end