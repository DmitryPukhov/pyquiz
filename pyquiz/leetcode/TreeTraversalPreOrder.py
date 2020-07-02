from pyquiz.common.TreeNode import TreeNode


class TreeTraversalPreOrder:
    @staticmethod
    def traverse_iterative(root: TreeNode) -> []:
        """
        Iterative tree traversal pre order
        """
        out, stack = [], []
        node = root
        while True:
            # Go left
            while node:
                # Out node and go left
                out.append(node.val)
                stack.append(node)
                node = node.left
            if not stack:
                break
            # Get the node from stack and go right
            node = stack.pop()
            node = node.right
        return out

    def traverse_recursive(self, root: TreeNode) -> []:
        """
        Recursive tree traversal in order
        """
        out = []
        if root:
            # Go in order: left, current, right
            out.append(root.val)
            out += self.traverse_recursive(root.left)
            out += self.traverse_recursive(root.right)
        return out
