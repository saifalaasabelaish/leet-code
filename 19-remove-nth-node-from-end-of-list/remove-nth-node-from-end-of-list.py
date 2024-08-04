# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return None    
        dummy = ListNode(0)
        dummy.next = head
        tracker = dummy
        length = 0
        
        while tracker.next:
            length += 1
            tracker = tracker.next
        
        stop_pos = length - n
        tracker = dummy 
        
        for i in range(stop_pos):
            tracker = tracker.next
        
        tracker.next = tracker.next.next
        
        return dummy.next
