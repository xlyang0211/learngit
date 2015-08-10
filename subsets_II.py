__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        res = [[]]
        subset = []
        nums = sorted(nums)
        print nums
        for index in xrange(len(nums)):
            subset = []
            self.dfs(res, subset, index, nums)
        return res

    def dfs(self, res, subset, index, nums):
        for i in xrange(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            res.append(subset)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 0]
    solution = Solution()
    print solution.subsetsWithDup(nums)