__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        temp_max_sum = float('-inf')
        for i in xrange(len(nums)):
            if temp_max_sum < 0:
                temp_max_sum = nums[i]
            else:
                temp_max_sum += nusm[i]
                if temp_max_sum > max_sum:
                    max_sum = temp_max_sum
        return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print solution.maxSubArray(nums)