# max depth of binary tree
# 1. DFS 2. BFS 3. recursive function

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1, recursive solution
        # 1 + max(dfs(left), dfs(right))
        
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

        # 2. bfs
        # depth = how much BFS is called
        # if not root:
        #     return 0
        
        # level = 1
        # q = deque([root])
        # while q:
        #     # traverse all children
        #     for i in range(len(q)):
        #         node = q.poplist()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # 3. iterative DFS
        # when node is pop, update level if necessary
        stack = [[root, 1]]
        root = 0
        
        while stack:
            node, depth = stack.pop()

            if node:
                # update result
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res