__author__ = 'seany'

# Note: The most important part is to devise the compare function, and pay special notice to it!

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        self.quick_sort(nums)
        return "".join([str(i) for i in nums])

    def compare(self, a, b):
        """
        return 1 if a is "bigger" than b;
        return 0 if a is equal to b;
        return -1 if a is "smaller" than b;
        e.g.: 35 is "bigger" than 340, 222 is "bigger" than 2 ...
        :param a: str to represent a number
        :param b: str to represent a number
        :return: 1, 0, -1 to represent the comparing result
        """
        if int(a + b) > int(b + a):
            return 1
        elif int(a + b) < int(b + a):
            return -1
        else:
            return 0

    def quick_sort(self, nums):
        self.__quick_sort(0, len(nums), nums)

    def __quick_sort(self, start, end, nums):
        print nums
        print start, end
        if start >= end - 1:  # There is (are) 1 or 2 element in the sequence to be sorted;
            return
        i = start - 1
        pivot = nums[end - 1]
        for j in xrange(start, end):
            if self.compare(str(pivot), str(nums[j])) == -1:
                print "enter here"
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
        nums[i + 1], nums[end - 1] = nums[end - 1], nums[i+1]
        self.__quick_sort(start, i + 1, nums)
        self.__quick_sort(i + 2, end, nums)


if __name__ == "__main__":
    a = "35"
    b = "340"
    #solution = Solution()
    #print solution.compare(a, b)
    nums = [1, 2, 3, 1]
    solution = Solution()
    print solution.largestNumber(nums)