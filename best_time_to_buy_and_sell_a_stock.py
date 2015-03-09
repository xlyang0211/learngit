class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return False
        min = prices[0]
        diff = 0
        for i in xrange(1, len(prices)):
            if prices[i] < min:   # It's no matter that the if is before the latter one or after it.
                min = prices[i]
            if prices[i] - min > diff:  # At this time the min must be the price that before the current prices[i]
                diff = prices[i] - min
        return diff

if __name__ == "__main__":
    list = [1111, 5, 23, 904, 23, 22, 919]
    solution = Solution()
    print solution.maxProfit(list)

# The algorithm above apparently works well with the desired result, but to output the desired index is not so well
# supported, and the algorithm is not so directed at first glance, comparing with the algorithm i read before.
