# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l + r <= distance:
                        count += 1

            return [n+1 for n in (left+right) if n+1 < distance]

        dfs(root)
        return count
