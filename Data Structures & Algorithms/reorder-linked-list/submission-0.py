# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        mid, end = head, head.next
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        # reverse the second half

        curr = mid.next
        prev = mid.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # merge -> prev is at the end of the list, head at the beginning

        first, second = head, prev

        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
        
