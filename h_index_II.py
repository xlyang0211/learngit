__author__ = 'seany'

# citations is sorted in ascending order;

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        h_index = 0
        length = len(citations)
        for i in xrange(length):
            if length - i <= citations[i]:
                h_index = length - i
                break
        return h_index

if __name__ == "__main__":
    solution = Solution()
    lst = sorted([5, 5, 0, 11, 23, 2, 8], reverse=False)
    print lst
    print solution.hIndex(lst)