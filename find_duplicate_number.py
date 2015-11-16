__author__ = 'seany'

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_duplicate_number(1, len(nums), nums)

    def find_duplicate_number(self, start, end, nums):
        if start == end:
            return start
        count = 0
        pivot = (start + end) / 2
        for i in nums:
            if start <= i <= pivot:
                count += 1
        if count > pivot - start + 1:
            return self.find_duplicate_number(start, pivot, nums)
        else:
            return self.find_duplicate_number(pivot + 1, end, nums)

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2]
    print solution.findDuplicate(nums)