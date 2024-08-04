# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head == None or head.next == None :
            return head 
        odd_list = ListNode(0) 
        odd_ptr = odd_list
        even_list = ListNode(0)
        even_ptr = even_list 
        index = 1 
        while head != None :
            if index % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            head = head.next
            index+=1
        even_ptr.next = None
        odd_ptr.next = even_list.next
        return odd_list.next