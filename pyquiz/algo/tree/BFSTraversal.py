from pyquiz.common.TreeNode import TreeNode


class BFSTraversal:
    """
    Traverse binary tree using BFS - Breadth first search algorithm
    """

    def bfs(self, root: TreeNode) -> []:
        """
        Traverse the tree using BFS, return values
        """
        if not root:
            return []
        out = []
        q = [root]
        while q:
            node = q.pop(0)
            out.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return out
