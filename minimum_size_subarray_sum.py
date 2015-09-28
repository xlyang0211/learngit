__author__ = 'seany'

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        local_max = 0
        start = 0
        end = 0
        max_sum_length = len(nums) + 1
        while end < len(nums):
            while end < len(nums) and local_max < s:
                local_max += nums[end]
                end += 1
            end -= 1
            print "end is:", end
            while local_max >= s:
                local_max -= nums[start]
                start += 1
            start -= 1  # Get the last start that makes local_max bigger than s;
            print "start is:", start
            max_sum_length = min(max_sum_length, end - start + 1)
            start = end + 1  # update start;
            end += 1
        return max_sum_length

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    print solution.minSubArrayLen(7, nums)