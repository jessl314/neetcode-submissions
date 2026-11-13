# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        heights = {None: 0}
        max_diameter = 0

        while stack:
            node = stack[-1]

            # Ensure both children have been processed
            left_done = node.left in heights
            right_done = node.right in heights

            if left_done and right_done:
                stack.pop()
                left_h = heights[node.left]
                right_h = heights[node.right]

                # 1. Update max diameter passing through current node
                max_diameter = max(max_diameter, left_h + right_h)

                # 2. Store current node's height
                heights[node] = 1 + max(left_h, right_h)
            else:
                # Push right first, then left (so left is processed first)
                if node.right and node.right not in heights:
                    stack.append(node.right)
                if node.left and node.left not in heights:
                    stack.append(node.left)

        return max_diameter