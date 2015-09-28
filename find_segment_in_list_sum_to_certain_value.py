__author__ = 'seany'
# An problem mentioned on the internet:
# for a data list, find the number of sequence in the list which comply with following requirements:
# 1. the sequence should continuous;
# 2. the sum of the sequence is zero;
# Solution is as following:


from collections import defaultdict
class FindSegment:
    def get_segment(self, lst):
        if not len(lst):
            return 0
        else:
            sum_list = []
            sum = 0
            for i in lst:
                sum += i
                sum_list.append(sum)
            print sum_list
            sum_hash = defaultdict(int)
            for i in sum_list:
                sum_hash[i] += 1
            ret = 0
            for i in sum_hash:
                if sum_hash[i] > 1:
                    ret += (sum_hash[i] - 1)
                if i == 0:
                    ret += 1
            return ret

if __name__ == "__main__":
    segment = FindSegment()
    lst = [0, 1, 1, 3, -4, 2, 5, -7, -1]
    print lst
    print segment.get_segment(lst)