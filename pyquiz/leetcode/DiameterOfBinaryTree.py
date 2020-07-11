from pyquiz.common.TreeNode import TreeNode


class DiameterOfBinaryTree:
    d = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0
        t = max(self.traverse(root))
        max(self.d, t)

    def traverse(self, node: TreeNode) -> int:
        if not node: return 0
        er = self.traverse(node.left)+1 if node.left else 0
        el = self.traverse(node.right)+1 if node.right else 0
        self.d = max(self.d, el, er, el+er)
        return max(el,er)
