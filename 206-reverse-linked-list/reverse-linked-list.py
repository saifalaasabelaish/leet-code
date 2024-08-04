# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            reversed_list = None
            current = head
            while current:
                next_node = current.next
                current.next = reversed_list
                reversed_list = current
                current = next_node
    
        return reversed_list
        