__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        index = 0
        sub_index = 0
        sum = 0
        current_set = []
        set_list = []
        n_sum = 4
        if len(nums) < n_sum:
            return set_list
        else:
            return self.get_four_sum(sorted(nums), target, n_sum, 0, 0, 0, current_set, set_list)

    def get_four_sum(self, nums, target, n_sum, sum, sub_index, index, current_set, set_list):
        if sub_index < n_sum - 2:
            for i in xrange(index, len(nums)-2+sub_index):
                self.get_four_sum(nums, target, n_sum, sum + nums[i], sub_index+1, i+1, current_set + [nums[i]], set_list)
        else:
            i = index
            j = len(nums) - 1
            while i < j:
                if sum + nums[i] + nums[j] < target:
                    i += 1
                elif sum + nums[i] + nums[j] > target:
                    j -= 1
                else:
                    temp_list = current_set + [nums[i], nums[j]]
                    if temp_list not in set_list:
                        set_list.append(temp_list)
                    i += 1
                    j -= 1
        return set_list

if __name__ == "__main__":
    nums = [-1, 1, 0, 0, -2, 1]
    solution = Solution()
    print solution.fourSum(nums, -1)