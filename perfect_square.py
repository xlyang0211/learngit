__author__ = 'seany'

# Dynamic programming is used here to get the minimum count of squares to summing up to n;
# Pay attention to the key point that matters is that 12 is composed of 4, 4, 4 instead of 9, 1, 1, 1;

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = n
        count = 0
        # dynamic programming is used here to get value
        count_list = [float('inf')] * (n + 1)
        count_list[0] = 0
        for i in xrange(n + 1):
            if not i:
                continue
            j = 0
            while j ** 2 <= i:
                count_list[i] = min(count_list[i], count_list[i - j ** 2] + 1)
                j += 1
        return count_list[n]

if __name__ == "__main__":
    solution = Solution()
    print solution.numSquares(5)