# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global max_depth
        max_depth = 0
        def dfs(node, depth ):
            global max_depth
            if node is None:
                # print(f"{depth, max_depth}")
                if max_depth < depth:
                    max_depth = depth
                return
            else:
                # print(f"{root.val}노드 방문{depth, max_depth}", )
                depth +=1
                dfs(node.left, depth)
                dfs(node.right, depth)
        dfs(root, 0)
        return max_depth