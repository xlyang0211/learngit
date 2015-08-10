__author__ = 'seany'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if root is None:
            return 0
        return self.get_value(root, 0)

    def get_value(self, root, current_value):
        if root.left is None:
            if root.right is None:
                return 10 * current_value + root.val
            else:
                return self.get_value(root.right, 10 * current_value + root.val)
        else:
            if root.right is None:
                return self.get_value(root.left, 10 * current_value + root.val)
            else:
                return self.get_value(root.left, 10 * current_value + root.val) + self.get_value(root.right, 10 * current_value + root.val)