__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        start = 0
        end = len(nums) - 1
        rang = [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return rang
        else:
            rang[0] = self.get_left(nums, target, start, end)
            rang[1] = self.get_right(nums, target, start, end)
            return rang

    def get_left(self, nums, target, start, end):
        if start == end:
            return start
        elif start + 1 == end:
            if nums[start] == nums[end]:
                return start
            else:
                if target == nums[end]:
                    return end
                else:
                    return start
        else:
            mid = (start + end) / 2
            if target <= nums[mid]:
                return self.get_left(nums, target, start, mid)
            else:
                return self.get_left(nums, target, mid, end)

    def get_right(self, nums, target, start, end):
        if start == end:
            return start
        elif start + 1 == end:
            if nums[start] == nums[end]:
                return end
            else:
                if target == nums[start]:
                    return start
                else:
                    return end
        else:
            mid = (start + end) / 2
            if target < nums[mid]:
                return self.get_right(nums, target, start, mid)
            else:
                return self.get_right(nums, target, mid, end)

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3]
    print solution.searchRange(nums, 1)

# This question is different from ¡®search_for_a_range.py¡¯ that it finds the smallest range in the nums that contains target numbers;