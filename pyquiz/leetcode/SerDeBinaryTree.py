from collections import deque

from pyquiz.common.TreeNode import TreeNode


class SerDeBinaryTree:
    """
    Serialize and Deserialize Binary Tree
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

    Example 1:
       1
     /  \
    2    3
        / \
       4   5
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

    Example 2:
    Input: root = []
    Output: []
    Example 3:

    Input: root = [1]
    Output: [1]

    Example 4:
    Input: root = [1,2]
    Output: [1,2]

    Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        nextlevel = deque([root])
        out = [str(root.val)]
        isempty = False

        while not isempty:
            level = nextlevel
            nextlevel = deque()
            isempty = True
            while level:
                # Form next level
                node = level.popleft()
                if not node:
                    continue
                nextlevel.extend([node.left, node.right])
                isempty = isempty and (node.left is None) and (node.right is None)
            if not isempty:
                out.extend([n.val if n else 'null' for n in nextlevel])
        return ','.join([str(x) for x in out])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = deque(data.split(','))
        root = TreeNode(int(data.popleft()))
        nextlevel = deque([root])

        while data:
            level = nextlevel
            nextlevel = deque()
            while level and data:
                node = level.popleft()
                if not node:
                    continue
                # Get left
                leftstr = data.popleft()
                leftval = int(leftstr) if leftstr != 'null' else None
                if leftval is not None:
                    node.left = TreeNode(leftval)
                nextlevel.append(node.left)
                if data:
                    # Get right
                    rightstr = data.popleft()
                    rightval = int(rightstr) if rightstr != 'null' else None
                    if rightval is not None:
                        node.right = TreeNode(rightval)
                    nextlevel.append(node.right)

        return root
