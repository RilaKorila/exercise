# definition for a Node
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node'):
        # nodes which is already copied
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                # node is already cloned
                return oldToNew[node]
            
            # in the case that node in not cloned yet
            # we have to clone node (= make new instance)
            copy = Node(node.val)
            oldToNew[node] = copy

            # check neighbors of original node 
            for nei in node.neighbors:
                # dfs(nei) returns clone of node
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
        