# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        321
        987
        1308

        digit will be the sum if sum < 10
        else it is sum // 10
        carry if sum >= 10 is sum % 10
        
        
        """
        carry = 0
        c1 = l1
        c2 = l2
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            digit_sum = val1 + val2 + carry
            digit = digit_sum % 10
            carry = digit_sum // 10
            curr.next = ListNode(digit)
        
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

