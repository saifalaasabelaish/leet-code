class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
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