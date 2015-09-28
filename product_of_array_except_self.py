__author__ = 'seany'

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left_list = [1] * length
        right_list = [1] * length
        ret = [0] * length
        left = 1
        right = 1
        for i in xrange(1, length):
            j = length - i - 1
            left *= nums[i - 1]
            right *= nums[j + 1]
            left_list[i] = left
            right_list[j] = right
        print left_list
        print right_list
        for i in xrange(length):
            ret[i] = left_list[i] * right_list[i]
        return ret

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0]
    print solution.productExceptSelf(nums)