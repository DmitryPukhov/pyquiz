from typing import List


class InMemoryFileSystem:
    """
    588. Design In-Memory File System
    Design an in-memory file system to simulate the following functions:
    ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and direc
    mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you
    addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file alr
    readContentFromFile: Given a file path, return its content in string format.
    Example:
    Input:
    ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
    [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
    Output:
    [null,[],null,null,["a"],"hello"]
    Explanation:
    filesystem
    Note:
    You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
    You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
    You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
    """


    class Node:
        """
        File system node: directory or file
        """

        def __init__(self, name: str):
            self.name = name
            self.file: str = None
            self.children = {}
            pass

    def __init__(self):
        self.root = self.Node(None)

    def ls(self, path: str) -> List[str]:
        node = self._getnode(path.split('/'))
        if node and node.file:
            return [node.name]

        return sorted(list(node.children.keys())) if node else []

    def mkdir(self, path: str) -> None:
        names = path.split('/')[1:]
        node = self.root
        for name in names:
            if name not in node.children:
                node.children[name] = self.Node(name)
            node = node.children[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split('/')
        dir = self._getnode(path[:-1])

        filename = path[-1]
        if filename not in dir.children:
            filenode = self.Node(filename)
            filenode.file = content
            dir.children[filename] = filenode
        else:
            dir.children[filename].file += content

    def readContentFromFile(self, filePath: str) -> str:
        filenode = self._getnode(filePath.split('/'))
        return filenode.file if filenode else None

    def _getnode(self, path: List[str]) -> Node:
        node = self.root
        for name in path[1:]:
            if not name:
                return node
            if name not in node.children:
                return None
            node = node.children[name]
        return node

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
