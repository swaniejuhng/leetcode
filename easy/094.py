# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # my solution
        inorder = []
        helper(root, inorder)
        return inorder


def helper(node, result):
    if node:
        helper(node.left, result)
        result.append(node.val)
        helper(node.right, result)
