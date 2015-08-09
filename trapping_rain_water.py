class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        A_tmp = [0] * len(A)
        left_max = 0
        #  First record the left max of each node;
        for i in xrange(len(A)):
            A_tmp[i] = left_max
            if A[i] > left_max:
                left_max = A[i]
        #  Second record the right max of each node, if right max is less than left max, get left max;
        right_max = 0
        for i in xrange(len(A)-1, -1, -1):
            if A_tmp[i] > right_max:
                A_tmp[i] = right_max
            if A[i] > right_max:
                right_max = A[i]
        area = 0
        for i in xrange(len(A)):
            if A_tmp[i] > A[i]:
                area += A_tmp[i] - A[i]
            else:
                pass
        return area


if __name__ == "__main__":
    lst = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print solution.trap(lst)

#  The most difficult part of the problem is that how to analyze the method of calculating the trapping water:
#  We need to generalize the nodes
#  For each node, what's the key factor that decide the amount of water it can trap?
#  For certain node:
#  1. we find the max height of its left;
#  2. we find the max height of its right;
#  3. we calculate the min(left_max, right_max);
#  4. we compare min(left_max, right_max) with height of that node to see:
#     if former is bigger than latter, it can trap (min(left_max, right_max)-h(node)) water;
#     otherwise, no water trapped of the node;