__author__ = 'seany'

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        lst = []
        l_lst = []
        if 9 * k < n:
            pass
        else:
            self.dfs(0, k, n, lst, l_lst)
        return l_lst

    def dfs(self, i, k, n, lst, l_lst):
        if i == k - 2:
            if n - sum(lst) <= 17:
                start = 0
                if k != 2:
                    start = lst[-1]
                end = 8  # which represent the index of 9 in [1, 2, 3, 4, 5, 6, 7, 8, 9]
                while start < end:
                    if start == end:
                        break
                    elif start + 1 + end + 1 < n - sum(lst):
                        start += 1
                    elif start + 1 + end + 1 > n - sum(lst):
                        end -= 1
                    else:
                        l_lst.append(lst + [start + 1, end + 1])
                        start += 1
                        end -= 1
        else:
            begin = 0
            if len(lst):
                begin = lst[-1]
            for a in xrange(begin, 9):
                self.dfs(i + 1, k, n, lst + [a + 1], l_lst)

if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum3(4, 22)