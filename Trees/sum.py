# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
        
    #     stack = [root]
    #     def dfs():
    #         while stack:
                
            
            
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False
            
            curSum += node.val
            # whether cur node is leaf node
            if not node.left and node.right:
                return curSum == self.targetSum
            
            return (dfs(node.left, curSum)  or dfs(node.right, curSum))
        return dfs(root, 0)
            
            
                