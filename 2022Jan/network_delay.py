# use Dijkstra's algorithm
# Difference between BFS and Dijkstra is for Dijkstra uses Minimum Heap(Priority Queue)

class Solution:
    def networkDelayTime(self, times: List[List[int], n: int, k:int]) -> int:
        edges = collections.defaultdict(list)

        # u: node
        # v: neighbor of node v
        # w: weight of the edge btw u and v
        for u, v, w in times:
            edges[u].append((v, w))

        #  k: start node
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            # heapq.heappop(minHeap): pick up min value from minHeap
            # w1: weight, n1: node

            w1, n1 = heapq.heappop(minHeap)
            # if n1 is already visited
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            # n2: all neighbors of n1 node
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        # len(visit) == n: we can't visit every single node
        return t if len(visit) == n else -1
