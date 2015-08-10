__author__ = 'seany'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        right_list = []
        self.get_list(root, 1, right_list)
        return right_list

    def get_list(self, root, layer, right_list):
        print layer
        if root is not None:
            if len(right_list) < layer:
                right_list.append(root.val)
            self.get_list(root.right, layer+1, right_list)
            self.get_list(root.left, layer+1, right_list)

if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    solution = Solution()
    print solution.rightSideView(head)

# Critial usage of DFS: