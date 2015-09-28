__author__ = 'seany'

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        duplicate_set = set([])
        for i in nums:
            if i not in duplicate_set:
                duplicate_set.add(i)
            else:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print solution.containsDuplicate(nums)
