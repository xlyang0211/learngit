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
            if target == nums[start]:
                return start
            else:
                return -1
        elif start + 1 == end:
            if nums[start] == nums[end]:
                if target == nums[start]:
                    return start
                else:
                    return -1
            else:
                if target == nums[end]:
                    return end
                elif target == nums[start]:
                    return start
                else:
                    return -1
        else:
            mid = (start + end) / 2
            if target <= nums[mid]:
                return self.get_left(nums, target, start, mid)
            else:
                return self.get_left(nums, target, mid, end)

    def get_right(self, nums, target, start, end):
        if start == end:
            if target == nums[start]:
                return start
            else:
                return -1
        elif start + 1 == end:
            if nums[start] == nums[end]:
                if target == nums[start]:
                    return end
                else:
                    return -1
            else:
                if target == nums[start]:
                    return start
                elif target == nums[end]:
                    return end
                else:
                    return -1
        else:
            mid = (start + end) / 2
            if target < nums[mid]:
                return self.get_right(nums, target, start, mid)
            else:
                return self.get_right(nums, target, mid, end)

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3]
    print solution.searchRange(nums, 2)

    # Please make sure you understand the subject of the question: found certain numbers, not the range of the number!!!