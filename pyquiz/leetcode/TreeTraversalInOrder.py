from pyquiz.common.TreeNode import TreeNode


class TreeTraversalInOrder:
    @staticmethod
    def traverse_iterative(root: TreeNode) -> []:
        """
        Iterative tree traversal in order
        """
        out, stack = [], []
        node = root
        while True:
            # Go left
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                break
            # Get the node from stack and go right
            node = stack.pop()
            out.append(node.val)
            node = node.right
        return out

    def traverse_recursive(self, root: TreeNode) -> []:
        """
        Recursive tree traversal in order
        """
        out = []
        if root:
            # Go in order: left, current, right
            out += self.traverse_recursive(root.left)
            out.append(root.val)
            out += self.traverse_recursive(root.right)
        return out
