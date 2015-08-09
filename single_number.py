class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        my_hash = {}
        for i in A:
            if i in my_hash:
                my_hash[i] += 1
            else:
                my_hash[i] = 0
        for i in A:
            if my_hash[i] == 0:
                return i
        return "Error encountered."

    def single_number(self, A):
        if len(A) % 2 == 0:
            return "Error."
        result = A[0]
        for i in A[1:]:
            result ^= i
        return result

solution = Solution()
lst = [6, 5, 6, 5, 6]
print solution.single_number(lst)

# Method 1 uses extra space;
# Method 2 uses linear time and no extra spaces (actually constant space: define result)
# two same numbers xor get 0;
# 0 xor with number N get N;
