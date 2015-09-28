__author__ = 'seany'
# A method to think twice:
# for the root node, s is "1";
# for a left children, add "0" to the end of s;
# for a right children, add "1" to the end of s;
# But how to get the biggest leaf node is the key point to solve the problem;
# A traditional method is to use dfs to traverse every node in the tree, but time complexity exceeds the limit;

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        tmp_root = root
        count = 0
        while tmp_root is not None:
            count += 1
            tmp_root = tmp_root.left
        last_str = ""

    def find_last(self, root, s):
        if root.right is not None:


    def bin2dec(self, s):
        count = 0
        ret = 0
        for i in reversed(s):
            if i == '1':
                ret += 2 ** count
            count += 1
        return ret

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.
    print solution.countNodes(root)