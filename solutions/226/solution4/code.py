# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        curr = root
        while curr:
            curr.left, curr.right = curr.right, curr.left
            curr = curr.left

        if root:
            curr = root.right

            while curr:
                curr.left, curr.right = curr.right, curr.left
                curr = curr.left

        return root