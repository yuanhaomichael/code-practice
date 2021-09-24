import heapq 
'''
For 2 sorted list, we can find the kth smallest by 2 pointers
for multiple sorted list, we can keep a pointer for each list
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        minHeap = []
        # only need to look at the first k rows because the 
        # columns are sorted. So min(k, N). 
        # Time O(min(K,N))
        for r in range(min(k,N)):
            # triplet(element, row, positon within list)
            minHeap.append((matrix[r][0], r, 0))
            heapq.heapify(minHeap)
        # Need to pop k-1 element to find the kth smallest
        # O(klog(min(K,N)))
        while k:
            # pop the smallest item from one of the sorted list
            element, r, c = heapq.heappop(minHeap)
            # push the next item from that list to the minHeap
            if c < N-1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            k-=1
            
        return element