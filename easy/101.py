# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diff_flag = False
    def isSymmetric(self, root: TreeNode) -> bool:
        # my solution
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.left and q.right:
                self.helper(p.left, q.right)
            elif (not p.left and q.right) or (p.left and not q.right):
                self.diff_flag = True
                return False

            if p.val != q.val:
                self.diff_flag = True
                return False

            if p.right and q.left:
                self.helper(p.right, q.left)
            elif (not p.right and q.left) or (p.right and not q.left):
                self.diff_flag = True
                return False

            return not self.diff_flag

        else:
            return not p and not q
    """

        def isSym(L, R):
            if (L and R) and (L.val == R.val):
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)
