# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        if not head.next :
            return False    
        visited = set()
        temp = head
        while temp:
            if temp.next and temp.next in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False