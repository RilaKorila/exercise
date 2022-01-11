class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List(str):
        # get empty list of source and distination
        adj = { src: [] for src, dst in tickets}

        # we want distination list of a smaller lexical order 
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            # finish condition: we visited all distination
            if len(res) == len(tickets) +1:
                return True
            # this src does not have any out going edges from it 
            if src not in adj:
                return False
            
            temp = list(adj[src]) # make a copy list (temporary array)
            # check our neighbor
            for i, v in enumerate(temp):
                # pop(i): the value at index is poped out and removed
                # adj[src]: next places list where we can go from src
                adj[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                
                # if dfs returns False, we have to back track the above dicision 
                adj[src].insert(i, v)
                # reverse the last dicision
                res.pop()
            return False
        

        dfs("JFK")
        return res

