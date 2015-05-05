class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        self.sort(candidates)



    def sort(self, list, b, c):
        """
        Use quick sort to sort candidates ascendingly.
        :param candidates: The list of integers
        :param b: beginning index
        :param c: last index
        :return: None
        """
        i = 0  # mark the next position that the element
        j = 0
        pivot = list[b]
        for i in xrange(b, c):
            j = i + 1
            if
