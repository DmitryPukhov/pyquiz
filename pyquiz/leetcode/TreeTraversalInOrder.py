from pyquiz.common.TreeNode import TreeNode


class TreeTraversalInOrder:
    @staticmethod
    def traverse(root: TreeNode) -> []:
        out, stack = [], []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                break
            node = stack.pop()
            out.append(node.val)
            node = node.right
        return out
