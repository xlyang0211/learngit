__author__ = 'seany'

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick_sort(nums, 0, len(nums), k)

    def quick_sort(self, nums, start, end, k):
        i = start - 1
        pivot = nums[end - 1]
        for j in xrange(start, end):
            if nums[j] > pivot:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
        print i, end
        nums[i + 1], nums[end - 1] = nums[end - 1], nums[i + 1]
        tmp = i - start + 2
        if tmp == k:
            return nums[i + 1]
        elif tmp < k:
            return self.quick_sort(nums, i + 2, end, k - tmp)
        else:
            return self.quick_sort(nums, start, i + 1, k)


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 5, 7]
    k = 2
    print solution.findKthLargest(nums, k)