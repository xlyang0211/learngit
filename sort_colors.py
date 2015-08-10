__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        i = self.quick_sort(nums, 0, len(nums)-1, 1)
        self.quick_sort(nums, i, len(nums)-1, 2)

    def quick_sort(self, nums, start, end, pivot):
        i = start - 1
        for j in xrange(start, end + 1):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i + 1


# This problem is solved easily by using the method used in quick sort;