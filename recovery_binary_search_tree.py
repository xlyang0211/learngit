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
                ��������£���root�����⻹��root.left�����⣿Ӧ�û���Ҫroot.right��ֵ���жϰɣ�
            else:
                recoverTree(root.left)
        if root.right is not None:
            if root.val > root.right.val:
                �����������root�����⻹��root.right�����⣿Ӧ�û���Ҫͨ��root.left��ֵ���жϰɣ�
            else:
                recoverTree(root.right)
        �����ҳ��˳�����������ط�����ôrecover������