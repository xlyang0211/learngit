class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        start = 0
        end = len(height) - 1
        max_area = 0
        while start != end:
