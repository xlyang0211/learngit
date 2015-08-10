__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        index = 0
        sub_index = 0
        sum = 0
        current_set = []
        set_list = []
        n_sum = 3
        if len(nums) < n_sum:
            return set_list
        else:
            return self.get_three_sum(sorted(nums), n_sum, 0, 0, 0, current_set, set_list)

    def get_three_sum(self, nums, n_sum, sum, sub_index, index, current_set, set_list):
        if sub_index < n_sum - 2:
            for i in xrange(index, len(nums)-2+sub_index):
                self.get_three_sum(nums, n_sum, sum + nums[i], sub_index+1, i+1, current_set + [nums[i]], set_list)
        else:
            i = index
            j = len(nums) - 1
            while i < j:
                print(i, j)
                if sum + nums[i] + nums[j] < 0:
                    i += 1
                elif sum + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    temp_list = current_set + [nums[i], nums[j]]
                    if temp_list not in set_list:
                        set_list.append(temp_list)
                    i += 1
                    j -= 1
        return set_list

if __name__ == "__main__":
    nums = [-2, 0, 1, 1, 2]
    solution = Solution()
    print solution.threeSum(nums)