import quick_sort
import time
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        solution = quick_sort.QuickSort()
        sorted_list = solution.quick_sort(num, 0, len(num)-1)
        left_num = sorted_list
        lst = []
        lst_of_lsts = []
        self.dfs(left_num, lst, lst_of_lsts)
        return lst_of_lsts

    def dfs(self, left_num, lst, lst_of_lsts):
        if len(left_num) == 0:
            if lst in lst_of_lsts:
                pass
            else:
                lst_of_lsts.append(lst)
        else:
            j = 0
            for i in xrange(len(left_num)):
                if i == 0:  # Line 24~30 is used for pruning the invalid branches of the permutation.
                    pass
                else:
                    if left_num[i] == left_num[j]:
                        continue
                    else:
                        pass
                left_num_tmp = left_num[:]
                lst_tmp = lst[:]
                lst_tmp.append(left_num[i])
                del left_num_tmp[i]
                self.dfs(left_num_tmp, lst_tmp, lst_of_lsts)
                j = i


if __name__ == "__main__":
    lst = [5, 2, 5, 2, 3, 4, 5, 4, 8, 9]
    my_solution = Solution()
    start = time.clock()
    for i in my_solution.permuteUnique(lst):
        print i
    end = time.clock()
    print "It costs %f seconds to run the program." % (end-start)





#  Solution 1:
#  1. If no duplications are taken into account, the num is result = (len(list))!;
#  2. Duplication counts, then the result should be divided, result = result / (duplication)!;

#  Solution 2:
#  1. Sort the list;
#  2. DFS; what's bfs here?

# Summary: The solution above may result in time limit excession.