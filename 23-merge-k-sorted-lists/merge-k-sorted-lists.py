import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, j in enumerate(lists):
            if j:
                heapq.heappush(heap, (j.val, i, j))
        temp = ListNode()
        cur = temp
        while heap:
            val, i, j = heapq.heappop(heap)
            cur.next = j
            cur = j
            j = j.next
            if j:
                heapq.heappush(heap, (j.val, i, j))
        return temp.next
    