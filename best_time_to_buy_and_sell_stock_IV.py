class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        """
        This solution is used for single buy and (possibly) multiply sell.
        just like [1, 2, 4], the result is 3, not 5;
        :param k:
        :param prices:
        :return:
        """
        length = len(prices)
        if k > length:
            return 0
        max_value = [0] * length
        max_diff = 0
        for i in xrange(length):
            if max_diff < prices[-(i+1)]:
                max_diff = prices[-(i+1)]
            max_value[-(i+1)] = max_diff

        diff_list = [max_value[i] - prices[i] for i in xrange(length)]
        k_index = self.find_k_largest(diff_list, 0, length-1, k)
        sum = 0
        for i in xrange(k_index, length):
            if diff_list[i] > 0:
                sum += diff_list[i]
        return sum

    def find_k_largest(self, diff_list, start, end, k):
        i = start - 1
        j = start
        pivot = diff_list[end]
        for j in xrange(start, end+1):
            if diff_list[j] < pivot:
                diff_list[i+1], diff_list[j] = diff_list[j], diff_list[i+1]
                i += 1
        diff_list[i+1], diff_list[end] = diff_list[end], diff_list[i+1]
        if end - i - 1 > k:
            return self.find_k_largest(diff_list, i+2, end, k)
        elif end - i - 1 == k:
            return i+2
        elif end - i == k:
            return i+1
        else:
            return self.find_k_largest(diff_list, start, i, k-(end-i))

if __name__ == "__main__":
    price_list = [1, 32, 323, 4, 23, 43, 23, 223, 224]
    solution = Solution()
    print solution.maxProfit(3, price_list)