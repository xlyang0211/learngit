__author__ = 'seany'

class Solution:
    def buy_and_sell_stocks(self, lst):
        lst_min = []
        min = lst[0]
        for i in lst:
            if i < min:
                min = i
            lst_min.append(min)
        max = 0
        print lst_min
        for i in xrange(len(lst)):
            if lst[i] - lst_min[i] > max:
                max = lst[i] - lst_min[i]
        return max

if __name__ == "__main__":
    lst = [2, 4, 5, 2, 12, 2, 4, 6, 8 , 23]
    solution = Solution()
    print solution.buy_and_sell_stocks(lst)