# Definition for a binary tree node.(二分木)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive solution
        # base case: both of node are leaves.
        if not p and not q:
            return True
        
        # only one of them is NULL
        if not p or not q:
            # each tree does not have same children
            return False
        
        # each  node does not have same node
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
