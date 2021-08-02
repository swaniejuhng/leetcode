# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # my solution
    diff_flag = False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # my solution
        if p and q:
            if p.left and q.left:
                self.isSameTree(p.left, q.left)
            elif (not p.left and q.left) or (p.left and not q.left):
                self.diff_flag = True
                return False

            if p.val != q.val:
                self.diff_flag = True
                return False

            if p.right and q.right:
                self.isSameTree(p.right, q.right)
            elif (not p.right and q.right) or (p.right and not q.right):
                self.diff_flag = True
                return False

            return self.diff_flag

        else:
            return not p and not q
