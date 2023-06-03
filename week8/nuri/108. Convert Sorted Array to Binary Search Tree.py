# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) < 1: return None
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root