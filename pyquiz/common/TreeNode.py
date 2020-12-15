from collections import deque
from typing import List, Deque


class TreeNode:
    """
    Binary tree node with left and right child
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __init__(self, val, parent=None, left=None, right=None):
    #     self.val = val
    #     self.parent = parent
    #     self.left = left
    #     self.right = right

    @staticmethod
    def of(bfs: List):
        """
        Construct from bfs list of values
        """
        root = TreeNode(bfs[0], None, None)
        level1: Deque[TreeNode] = deque([root])
        level2: Deque[TreeNode] = deque()
        ibfs = 1

        while level1:
            node = level1.popleft()
            if not node:
                continue
            node.left = TreeNode(bfs[ibfs]) if ibfs < len(bfs) and bfs[ibfs] is not None else None
            ibfs += 1
            node.right = TreeNode(bfs[ibfs]) if ibfs < len(bfs) and bfs[ibfs] is not None else None
            ibfs += 1
            level2.extend([node.left, node.right])
            if not level1:
                level1 = level2
                level2 = deque()

        return root

    def __str__(self):
        return str(self.val)


print(TreeNode.of([3,5,1,6,2,0,8,None,None,7,4]))
