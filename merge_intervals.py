<<<<<<< HEAD
#Definition for an interval.
=======
__author__ = 'seany'

# Definition for an interval.
>>>>>>> 1f33a455313b490408713921ee3fcc8211a33488
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
<<<<<<< HEAD
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

=======
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
>>>>>>> 1f33a455313b490408713921ee3fcc8211a33488
