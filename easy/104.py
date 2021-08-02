# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 0; max_depth = 0
    def maxDepth(self, root: TreeNode) -> int:
        # my solution - mine is better
        self.depth += 1

        if not root:
            self.depth -= 1
            return 0

        if root.left:
            self.maxDepth(root.left)

        self.max_depth = max(self.max_depth, self.depth)

        if root.right:
            self.maxDepth(root.right)

        self.depth -= 1
        return self.max_depth

        # better solution
        """
        return 1 + max(map(self.max_depth, (root.left, root.right))) if root else 0
        """
