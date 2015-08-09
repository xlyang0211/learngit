class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        # step one: find the biggest elements, what if there are negative integers?
        # Which means that counting sort cannot be used!
        # First let's assume all integers are positive:
        biggest = 0
        for i in num:
            if i > biggest:
                biggest = i
        lst = [0] * (biggest + 1)
        for i in num:
            lst[i] = 1
        consecutive = 0
        biggest_consecutive = 0
        for i in lst:
            if i == 1:
                consecutive += 1
            else:
                if consecutive > biggest_consecutive:
                    biggest_consecutive = consecutive
                consecutive = 0
        return biggest_consecutive

if __name__ == "__main__":
    lst = [200, 12, 2, 1, 5, 3, 4, 1]
    solution = Solution()
    print solution.longestConsecutive(lst)

# This solution is only for lst with positive integers, if there are negative integers (as the problem asked actually), memory error will
# appears.