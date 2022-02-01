# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find lowest common ancestor
        # Binary Tree: 
        # trees whose left node is lower than its parent's node, and right node is larger than its parent's one/
    
        cur = root

        while cur:
            # both of nodes exist right side
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # both of nodes exist left side
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            else:
                # one of children node is right side, and the other one is left side
                # in that case, current node is the common ancestor node of them
                return cur
