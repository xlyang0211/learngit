class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit_1(self, prices):
        """
        You can buy one unit every prices, so the max profit is fixed for certain prices list;
        """
        length = len(prices)
        sum = 0
        for i in xrange(length):
            max_diff = 0
            for j in xrange(i, length):
                diff = prices[j] - prices[i]
                if diff > max_diff:
                    max_diff = diff
            sum += max_diff
        return sum

    def maxProfit_2(self, prices):
        """
        You can buy one unit every prices, so the max profit is fixed for certain prices list;
        """
        length = len(prices)
        max_value = [0] * length
        max_diff = 0
        for i in xrange(length):
            if max_diff < prices[-(i+1)]:
                max_diff = prices[-(i+1)]
            max_value[-(i+1)] = max_diff
        max_profit = 0
        for i in xrange(length):
            diff = max_value[i] - prices[i]
            if diff > 0:
                max_profit += diff
        return max_profit


if __name__ == "__main__":
    price_list = [1, 32, 4, 323, 23, 43, 23, 223, 224]
    solution = Solution()
    print solution.maxProfit_1(price_list)
