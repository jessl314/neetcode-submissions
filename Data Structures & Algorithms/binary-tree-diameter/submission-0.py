# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # need to keep track of height in order to do sum of heights
        # diameter for each node as well -> iterative version
        # store in a map : node: (height, diameter)
        # use stack because we want longest path
        stack = [root]
        m = {None: (0, 0)} # avoid the empty dictionary issue

        while stack:
            # need both children in map (height tracked) in order to sum
            node = stack[-1]
            if node.left and node.left not in m:
                stack.append(node.left)
            elif node.right and node.right not in m:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = m[node.left]
                rightHeight, rightDiamter = m[node.right]
                m[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter + rightDiameter))
        return m[root][1]
