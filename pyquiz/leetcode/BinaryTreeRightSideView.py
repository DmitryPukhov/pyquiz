from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyquiz.common.TreeNode import TreeNode


class BinaryTreeRightSideView:
    """
    Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Example:
    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]

    Explanation:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    """

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque()
        q.extend([root,None])
        out = []
        lastnode=None
        while q:
            node: TreeNode = q.popleft()
            if not node:
                if lastnode and lastnode.val:
                    out.append(lastnode.val)
                if not q:
                    break
                q.append(None)
                continue
            else:
                lastnode=node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return out
