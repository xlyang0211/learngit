class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        """
        Only 2 transactions are allowed.
        """
        length = len(prices)
        max_value = [0] * length
        max_diff = 0
        for i in xrange(length):
            if max_diff < prices[-(i+1)]:
                max_diff = prices[-(i+1)]
            max_value[-(i+1)] = max_diff
        first_max_profit = 0
        second_max_profit = 0
        for i in xrange(length):
            diff = max_value[i] - prices[i]
            if diff > first_max_profit:
                second_max_profit = first_max_profit
                first_max_profit = diff
            elif second_max_profit < diff < first_max_profit:
                second_max_profit = diff
        return first_max_profit + second_max_profit

if __name__ == "__main__":
    price_list = [1, 32, 323, 4, 23, 43, 23, 223, 224]
    solution = Solution()
    print solution.maxProfit(price_list)