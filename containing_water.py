class Solution:
    def containing_most_water(self, height):
        if len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        max_water = min(height[left], height[right]) * (right - left)
        while left != right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if min(height[left], height[right]) * (right - left) > max_water:
                max_water = min(height[left], height[right]) * (right - left)
        return max_water

if __name__ == "__main__":
    height = [10,9,8,7,6,5,4,3,2,1]
    solution = Solution()
    print solution.containing_most_water(height)