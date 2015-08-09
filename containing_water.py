class Solution:
    def containing_water(self, lst):
        if len(lst) < 2:
            return 0
        left = 0
        right = len(lst) - 1
        max_water = 0
        while left != right:
            