class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in xrange(length):
            if nums[i] > 0 and nums[i] <= length:
                if nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # REally a wonderful solution!!!
        print "nums is:", nums
        for i in xrange(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

    def firstMissingPositive_1(self, nums):
        n = len(nums)
        for i in xrange(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                print nums[i]
                a = i
                b = nums[i] - 1
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # nums[a], nums[b] = nums[b], nums[a]  # This does works, but above line does not!!!
                print nums
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

if __name__ == "__main__":
    lst = [3, 4, -1, 1]
    solution = Solution()
    print solution.firstMissingPositive_1(lst)
