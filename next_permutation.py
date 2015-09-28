__author__ = 'seany'

# The algorithm is a little complicated, and it's narrated below:
# 1.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums) - 1, -1, -1):
            if i == 0:
                nums.sort()
            else:
                if nums[i] > nums[i - 1]:
                    mark = float('inf')
                    index = 0
                    for j in xrange(i, len(nums)):
                        if nums[i - 1] < nums[j] < mark:
                            mark = nums[j]
                            index = j
                    nums[i - 1], nums[index] = nums[index], nums[i - 1]
                    nums[:] = nums[:i] + sorted(nums[i:])
                    break

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    print nums

