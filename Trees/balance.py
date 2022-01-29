# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# if we start asking from root node, we have to ask if balanced on each node
# Time: O(n**2)  
# if we start asking from leaf node, we can do it only O(n)
# we can know height of current node immediately
class Solution:
    def idBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            # return [bool, height]
            if not root:
                return [True, 0]
            
            # recursive solution
            left, right = dfs(root.left), dfs(root.right)
            # bool: whether the tree is balanced
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1+max(left[1], right[1])]
        
        return dfs(root)

