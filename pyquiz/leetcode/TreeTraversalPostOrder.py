from pyquiz.common.TreeNode import TreeNode


class TreeTraversalPostOrder:
    @staticmethod
    def traverse_iterative(root: TreeNode) -> []:
        """
        Iterative tree traversal in order
        """
        out, stack = [], []
        # status: 0 - not visited, 1 - went left, 2 - went right
        node, status = root, 0
        while True:
            if not node:
                if stack:
                    node, status = stack.pop()
                else:
                    break

            if node and status == 0:
                # Go left
                while node:
                    stack.append((node, 1))
                    node, status = node.left, 0

            elif node and status == 1:
                # Have already been left, go right
                stack.append((node, 2))
                node, status = node.right, 0
            elif node and status == 2:
                out.append(node.val)
                if stack:
                    node, status = stack.pop()
                else:
                    break

        return out

    def traverse_recursive(self, root: TreeNode) -> []:
        """
        Recursive tree traversal in order
        """
        out = []
        if root:
            # Go in order: left, current, right
            out += self.traverse_recursive(root.left)
            out += self.traverse_recursive(root.right)
            out.append(root.val)
        return out
