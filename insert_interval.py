# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        new_intervals = []
        flag = 0
        for interval in intervals:
            print interval.start
            if newInterval.end < interval.start:
                if flag == 0:
                    new_intervals.append(newInterval)
                    flag = 1
                new_intervals.append(interval)
            elif interval.end < newInterval.start:
                new_intervals.append(interval)
            else:
                if newInterval.start < interval.start:
                    if interval.start <= newInterval.end <= interval.end:
                        new_intervals.append(Interval(newInterval.start, interval.end))
                        flag = 1
                    elif newInterval.end > interval.end:
                        pass
                elif interval.start <= newInterval.start <= interval.end:
                    if newInterval.end <= interval.end:
                        new_intervals.append(interval)
                        flag = 1
                    else:
                        newInterval = Interval(interval.start, newInterval.end)
        if flag == 0:
            new_intervals.append(newInterval)
        return new_intervals

if __name__ == "__main__":
    intervals = []
    interval_1 = Interval(1, 3)
    interval_2 = Interval(4, 5)
    interval_3 = Interval(6, 9)
    intervals.append(interval_1)
    intervals.append(interval_2)
    intervals.append(interval_3)

    new_interval = Interval(2, 4)

    solution = Solution()
    new_intervals = solution.insert(intervals, new_interval)
    for i in new_intervals:
        print "New interval is: %d, %d" % (i.start, i.end)

# Combining with the previous problem: merge interval, it's also important to grasp using for loop to realize recussion;
