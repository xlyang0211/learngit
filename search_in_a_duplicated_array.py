class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        index_of_largest = self.search_largest(A, 0, len(A)-1)
        print "The index_of_largest is:", index_of_largest
        if index_of_largest == len(A)-1:
            return self.search_element(A, 0, index_of_largest, target)
        else:
            if target >= A[0]:
                return self.search_element(A, 0, index_of_largest, target)
            else:
                return self.search_element(A, index_of_largest+1, len(A)-1, target)

    def search_largest(self, A, b, c):
        """ Find the index of the largest value in the rotated array
        :param A: The rotated array
        :param b: The index of the first element in the rotated array
        :param c: The index of the last element in the rotated array
        :return: The index of the largest element
        """
        if b == c:
            return b
        if b + 1 == c:  # If there is no this branch, else branch can't figure out within 2 elements;
                        # This is actually the boundary problem that it can not converge to 1, but only can
                        # converge to 2, so sub-list with 2 elements are also required to deal separately;
            if A[b] > A[c]:
                return b
            else:
                return c
        else:
            mid = (b + c) / 2
            if A[mid] >= A[b] and A[mid] >= A[c]:
                return self.search_largest(A, mid, c)
            elif A[mid] < A[b] and A[mid] < A[c]:
                return self.search_largest(A, b, mid)
            else:
                return c

    def search_element(self, A, b, c, target):
        """  For a sorted array, find the target value in it or return -1;
        :param A: The array;
        :param b: The index of the first element in search scope
        :param c: The index of the last element in search scope
        :param target: The target value;
        :return: The index of the target value in the array or -1 for not finding it;
        """
        if b == c:
            if target != A[b]:
                return -1
            else:
                return b
        elif b + 1 == c:
            if A[b] == target:
                return b
            elif A[c] == target:
                return c
            else:
                return -1
        else:
            mid = (b + c) / 2
            if target < A[mid]:
                return self.search_element(A, b, mid, target)
            else:
                return self.search_element(A, mid, c, target)

if __name__ == "__main__":
    solution = Solution()
    A = [4, 5, 8, 8.5, 9, 10, 1, 2]
    print solution.search(A, 2)

# Summary:
# 1. To solve the problem it will need O(logn) time complexity with divide and conquer;
# 2. First find the index of the largest element so as to make the array real sorted;
# 3. Second find (judge) if the target is in the array;
# 4. The most important part is to realize that sub array can not automatically converge from length of N (N > 2)
#    to 1 sometimes. It can only converge to 2 and then in the endless recursion. For example, [2, 4], mid = 0, if we take
#    [mid, c], it will be [2, 4] and then recursively... To deal with this situation, the algorithm need a elif branch to
#    deal with when length of sub-array is 2;