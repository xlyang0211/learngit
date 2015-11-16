__author__ = 'seany'

import sys

# For every int number, get it's 2-bit and calculate number of "1"s and "0"s at every ith index;

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        one_list = [0] * 32
        for i in nums:
            for j in xrange(32):
                one_list[j] += i % 2
                print one_list
                i /= 2
        print one_list
        for i in xrange(len(one_list)):
            if one_list[i] >= 3:
                one_list[i] %= 3
        str_list = ""
        print one_list
        for i in one_list:
            str_list += str(i)
        return int(str_list[::-1], 2)


if __name__ == "__main__":
    solution = Solution()
    print solution.singleNumber([1, 1, 1, 3, 3, 5, 5, 3, 5, 111])