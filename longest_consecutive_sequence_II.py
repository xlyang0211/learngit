__author__ = 'seany'

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_hash = {}
        for i in nums:
            if i + 1