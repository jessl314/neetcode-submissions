# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        m = {None: 0} # avoid the empty dictionary issue
        max_diameter = 0

        while stack:
            # need both children in map (height tracked) in order to sum
            node = stack[-1]
            if node.left in m and node.right in m:
                node = stack.pop()
                m[node] = 1 + max(m[node.left], m[node.right])
                max_diameter = max(max_diameter, m[node.left] + m[node.right])
            elif node.left not in m:
                stack.append(node.left)
            elif node.right not in m:
                stack.append(node.right)
                
        return max_diameter