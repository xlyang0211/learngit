__author__ = 'seany'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        new_citation = sorted(citations)[::-1]
        print new_citation
        h_index = 0
        for i in xrange(len(new_citation)):
            if i + 1 <= new_citation[i]:
                h_index = i + 1
        return h_index

if __name__ == "__main__":
    solution = Solution()
    lst = [2, 5, 0, 11, 23, 2, 8]
    print solution.hIndex(lst)