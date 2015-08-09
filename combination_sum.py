class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
<<<<<<< HEAD
        candidates.sort(reverse=False)
        print candidates
        lst = []
        result = []
        self.dfs(candidates, target, lst, result)
        return result

    def dfs(self, sorted_candidates, remain, lst, result):
        """
        dfs the sorted_candidates to find all combinations of number generating the result
        :param sorted_candidates:  The sorted candidates;
        :param remain:  number still in necessity;
        :param list: a list of possible combinations
        :param result: list of lists to store the final results;
        :return: None
        """
        count = 0
        for item in sorted_candidates:
            #  if remain > item:
            #      lst.append(item)  # this will lead to problem, because if it's added to lst,
                                     # in next iteration of "for", the remain is not changed;
            #      self.dfs(sorted_candidates, remain-item, lst, result)
            #  elif remain == item:
            #      lst.append(item)  # This also will lead to problem;
            #      result.append(lst)
            if remain > item:
                lst_tmp = lst[:]
                lst_tmp.append(item)
                self.dfs(sorted_candidates[count:], remain-item, lst_tmp, result)
            elif remain == item:
                lst_tmp = lst[:]
                lst_tmp.append(item)
                result.append(lst_tmp)
            count += 1

if __name__ == "__main__":
    my_list = [1, 2]
    target = 2
    solution = Solution()
    print solution.combinationSum(my_list, target)
=======
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
>>>>>>> 1f33a455313b490408713921ee3fcc8211a33488
