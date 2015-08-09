# The problem is a little tricky, and please make sure you understand it.
# Analysis: why this algorithm works?
# First original left and right are the two end of the list;
# Second, according to first, the residual rectangle has a more short length on x coordinate, so they
# must has a higher height to be the max_area candidates. That's the reason to determine when to incre-
# ment left or decrease right.
# The core question is that how to make sure the scan covers all the possibilities?
# Expression: If the max_area does exist, there must be a position that can be scanned!

class Solution:
    # @return an integer
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left != right:
            area = (right - left)*min(height[left], height[right])
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left+= 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    # Above method will be time limit exceeding. Please find ways to fix it properly.
    solution = Solution()
    print solution.maxArea([1, 1, 5, 2, 4, 5, 6])
