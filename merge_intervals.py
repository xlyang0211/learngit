#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        #  First sort the list of intervals according to its left value;
        new_intervals = self.sort(intervals)
        for i in xrange(new_intervals):
            if new_intervals[i].end

    def sort(self, intervals):
        self.quick_sort(intervals, 0, len(intervals))

    def quick_sort(self, lst, start, end):
        if end - start <= 1:
            return lst
        elif end - start == 2:
            if lst[0].start > lst[1].start:
                lst[0], lst[1] = lst[1], lst[0]
        else:
            i = -1
            j = 0
            pivot = lst[end].start
            for s in xrange(start, end):
                if lst[s].start < pivot:
                    lst[i+1], lst[s] = lst[s], lst[i+1]
                    i += 1
                else:
                    j += 1
            lst[end], lst[i+1] = lst[i+1], lst[end]
            self.quick_sort(lst, start, i)
            self.quick_sort(lst, i+1, end)

