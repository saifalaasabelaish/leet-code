# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack1 = []
        stack2 = []

     
        while l1:
            stack1.append(str(l1.val))
            l1 = l1.next

      
        while l2:
            stack2.append(str(l2.val))
            l2 = l2.next

        
        n1 = ''.join(stack1[::-1])  
        n2 = ''.join(stack2[::-1])

        total = str(int(n1) + int(n2))

    
        dummy = ListNode(0)
        current = dummy
        for digit in total[::-1]: 
            node = ListNode(int(digit))
            current.next = node
            current = current.next

        return dummy.next
