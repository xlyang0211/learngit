class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        length = len(A)
        i = 0
        while i < length:
            if 0 < A[i] < length and A[i] != i+1:
                tmp = A[i]
                A[i] = A[A[i]-1]
                A[tmp-1] = tmp
            else:
                i += 1
        for i in xrange(length):
            if A[i] != i+1:
                return i+1
        return length+1



solution = Solution()
print solution.firstMissingPositive([2, 3, 4, 1])

# Not done yet;