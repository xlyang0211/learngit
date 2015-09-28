__author__ = 'seany'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        kth_list = [0]
        self.dfs(root, k, kth_list)
        return kth_list[0]

    def dfs(self, root, k, kth_list):
        if root is None:
            return 0
        else:
            left = self.dfs(root.left, k, kth_list)
            if left >= kth_list:
                pass
            else:
                right = self.dfs(root.right, k - left - 1, kth_list)
            if left + right + 1 == k and kth_list[0] == 0:
                kth_list[0] = root.val
            return left + right + 1

if __name__ == "__main__":
    root = TreeNode(1)
    #root.left = TreeNode(3)
    root.right = TreeNode(2)
    #root.left.left = TreeNode(1)
    #root.left.right = TreeNode(4)
    #root.right.right = TreeNode(8)
    solution = Solution()
    print solution.kthSmallest(root, 1)