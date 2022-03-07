# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    # inorder: left->root->right
    # preorder: root->left->right
    # postorder: left->right->root
    
    def inorderWithoutRecursion(self, root: Optional[TreeNode])->List[int]:
        # solusion using stack: O(n)
        s = []
        cur = root
        res = []
        
        # traverse left side node until cur is NULL
        while True:
            if cur:
                s.append(cur)
                cur = cur.left
            
            # if current root is NULL and stack is not empty
            if not cur and s:
                cur = s.pop()
                res.append(cur.val)
                # ここをpopしたnodeのrightにしたい
                cur = cur.right
            
            # if current node is NULL and stack is empty
            elif not cur and not s:
                break
                
        return res

    # cf. https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
    def inorder(self, root: Optional[TreeNode])->List[int]:
        # solusion without recursive and stack: O(n)
        cur = root
        res = []
        
        while cur:
            # does not have left children
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            
            else:
                # have left children
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left

                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right            
        return res