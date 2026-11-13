"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        orig_to_copy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            orig_to_copy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = orig_to_copy[curr]
            copy.next = orig_to_copy[curr.next]
            copy.random = orig_to_copy[curr.random]
            curr = curr.next
        return orig_to_copy[head]        
        