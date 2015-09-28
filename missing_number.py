__author__ = 'seany'

# Analysis:
# Aim: O(n) time complexity;
#      O(1) space complexity;
# is the list sorted? Yes -> O(logn) time;
#                     No -> ???
#                     O(n) space? -> hash
# Final answer: actually this problem is pretty easy, result = sum of arithmetic progression minus sum of lst
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        elif len(nums) == 1:
            return 0
        else:
            return len(nums) * (len(nums) + 1) / 2 - sum(nums)

if __name__ == "__main__":
    lst = [0, 3, 2, 5, 1]
    solution = Solution()
    print solution.missingNumber(lst)