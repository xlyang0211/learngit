__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if len(nums) == 0:
            return True
        step = nums[0]
        for i in nums[1:]:
            if step > 0:
                step -= 1
                step = max(step, i)
            else:
                return False
        return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # nums = [3,2,1,0,4]
    solution = Solution()
    print solution.canJump(nums)


# This problem is very simple in writing algorithm, but very hard to understand the logic. It does not need to use dfs;