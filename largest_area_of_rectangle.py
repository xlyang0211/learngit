class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        left = 0
        right = len(height) - 1
        if right - left < 2:
            return 0
        left_max_list = [0] * len(height)
        right_max_list = [0] * len(height)
        for i in xrange(len(height)):
            if i == 0:
                left_max_list[i] = height[i]
            else:
                if left_max_list[i-1] > height[i]:
                    left_max_list[i] = left_max_list[i-1]
                else:
                    left_max_list[i] = height[i]
        for i in xrange(len(height)-1, -1, -1):
            if i == len(height) - 1:
                right_max_list[i] = height[i]
            else:
                if right_max_list[i+1] > height[i]:
                    right_max_list[i] = right_max_list[i+1]
                else:
                    right_max_list[i] = height[i]
        max_rain = 0
        for i in xrange(len(height)):
            if min(left_max_list[i], right_max_list[i]) - height[i] > 0:
                max_rain += min(left_max_list[i], right_max_list[i]) - height[i]
        return max_rain


if __name__ == "__main__":
    height = [10,9,8,7,6,5,4,3,2,4]
    solution = Solution()
    print solution.largestRectangleArea(height)