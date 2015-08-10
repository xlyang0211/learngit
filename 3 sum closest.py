__author__ = 'seany'

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums, target):
        num_list = sorted(nums)
        result = 0
        flag = True
        for i in xrange(len(num_list) - 2):
            first = num_list[i]
            s = i + 1
            t = len(num_list) - 1
            while s < t:
                sum = first + num_list[s] + num_list[t]
                if flag:
                    result = sum
                    flag = False
                else:
                    if abs(target - sum) < abs(target - result):
                        result = sum
                if target > sum: # Here why not compare abs(target - sum) with abs(target - result) ???
                    s += 1
                elif target < sum:
                    t -= 1
                else:
                    return target
        return result



if __name__ == "__main__":
    nums = [0, 0, 0]
    solution = Solution()
    print solution.threeSum(nums, 1)