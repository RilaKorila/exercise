import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        # minHeap of K-size is enough
        # minimum node of this heap is result, Kth largest node
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        

    def add(self, val: int) -> int:
        # insert val to Heap
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            # pop minimum node in Heap
            # minimun node in Heap means K+1th largest node
            heapq.heappop(self.minHeap)
        
        # root node is the minimum node in minHeap
        return self.minHeap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
