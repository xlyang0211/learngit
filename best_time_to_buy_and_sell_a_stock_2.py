class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        profit_this_time = 0
        while 1:
            if len(prices) < 2:
                profit_this_time = 0
            else:
                profit_this_time, prices = self.maxProfitWithOnePair(prices)
                print prices
                if profit_this_time <= 0:
                    break
                else:
                    profit += profit_this_time
        return profit

    def maxProfitWithOnePair(self, prices):
        min_index = 0
        min_index_pseudo = 0
        max_index = 0
        diff = 0
        for i in xrange(1, len(prices)):
            if prices[i] < prices[min_index_pseudo]:   # It's no matter that the if is before the latter one or after it.
                min_index_pseudo = i
            if prices[i] - prices[min_index_pseudo] > diff:  # At this time the min must be the price that before the current prices[i]
                diff = prices[i] - prices[min_index_pseudo]
                min_index = min_index_pseudo
                max_index = i
        print prices
        print min_index
        print max_index
        del prices[min_index]
        del prices[max_index-1]
        return diff, prices

if __name__ == "__main__":
    list = [1111, 5, 23, 904, 23, 22, 919]
    solution = Solution()
    print solution.maxProfit(list)

# Summary: This problem is a little hard to comprehend for what does it mean by a deal!!!