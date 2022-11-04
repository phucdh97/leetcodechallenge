# Definition for a binary tree node.
import collections
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val=1)
            node.left = root
            return node

        
        q = deque()
        level = 0
        q.append((root, 1))
        while q:
            node, level = q[0]
            if level == depth -1:
                break
            else:
                q.popleft()

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        
        for node in q:
            if node.left:
                temp = node.left
                new_node = TreeNode(val=1)
                node.left = new_node
                new_node.left = temp

            if node.right:
                temp = node.right
                new_node = TreeNode(val=1)
                node.right = new_node
                new_node.right = temp

        return root