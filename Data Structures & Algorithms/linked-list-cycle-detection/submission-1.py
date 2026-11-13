# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

"""
think about it this way: 

- the fast pointer moves twice as far as the slow pointer in an iteration. moving slow pointer
by one node, fast moves by two nodes.
- if we have a cycle (a circle) -> than when the slow pointer has traveled "half a circle" the fast pointer
will have traveled a "full circle", two semi-circles = a full circle and two full circles will arrive at same 
destination/time as one full circle




"""