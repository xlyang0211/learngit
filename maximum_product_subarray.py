__author__ = 'xlyang0211'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if len(nums) == 0:
            return
        else:
            local_max = nums[0]
            local_min = nums[0]
            global_max = nums[0]
            for i in xrange(1, len(nums)):
                l_max = local_max # to avoid in line 17 that local_min get its value using new local_max;
                l_min = local_min
                local_max = max(l_max * nums[i], l_min * nums[i], nums[i])
                local_min = min(l_max * nums[i], l_min * nums[i], nums[i])
                global_max = max(global_max, local_max)
            return global_max

if __name__ == "__main__":
    solution = Solution()
    nums = [-4, -3, -2]
    print solution.maxProduct(nums)