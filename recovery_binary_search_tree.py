# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        if root.left is not None:
            if root.val < root.left.val:
                这种情况下，是root的问题还是root.left的问题？应该还需要root.right的值来判断吧？
            else:
                recoverTree(root.left)
        if root.right is not None:
            if root.val > root.right.val:
                这种情况下是root的问题还是root.right的问题？应该还需要通过root.left的值来判断吧？
            else:
                recoverTree(root.right)
        即便找出了出错误的两个地方，怎么recover？？？