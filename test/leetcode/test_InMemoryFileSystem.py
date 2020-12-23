from unittest import TestCase

from pyquiz.leetcode.InMemoryFileSystem import InMemoryFileSystem


class TestFileSystem(TestCase):
    def test_example1(self):
        """
        Input:
        ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
        [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

        Output:
        [null,[],null,null,["a"],"hello"]
        """
        fs = InMemoryFileSystem()
        self.assertEqual([],fs.ls("/a/b/c"))

        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d","hello")
        self.assertEqual(["a"], fs.ls("/"))

        self.assertEqual("hello",fs.readContentFromFile("/a/b/c/d"))
        self.assertEqual(["d"], fs.ls("/a/b/c/d"))

    def test_createfilewithdirs(self):
        fs = InMemoryFileSystem()
        fs.addContentToFile("/a/b/c", "content1")
        self.assertEqual("content1", fs.readContentFromFile("/a/b/c"))

    def test_ls_root(self):
        fs = InMemoryFileSystem()
        #fs.mkdir("/")
        self.assertEqual([], fs.ls("/"))

    def test_mkdir_root(self):
        fs = InMemoryFileSystem()
        fs.mkdir("/")

    def test_mkdir_a_cb(self):
        fs = InMemoryFileSystem()
        fs.mkdir("/a/c")
        fs.mkdir("/a/b")
        bc = fs.ls("/a")
        self.assertEqual(["b", "c"], bc)

    def test_mkdir_a_b_c(self):
        fs = InMemoryFileSystem()
        fs.mkdir("/a/b/c")
        self.assertEqual(["b"], fs.ls("/a"))
        self.assertEqual(["c"], fs.ls("/a/b"))

    def test_add_content_to_file(self):
        fs = InMemoryFileSystem()
        fs.mkdir("/a")
        fs.addContentToFile("/a/file1.txt", "line1\n")
        fs.addContentToFile("/a/file1.txt", "line2\n")
        self.assertEqual("line1\nline2\n", fs.readContentFromFile("/a/file1.txt"))

    def test_read_content_from_file_root(self):
        fs = InMemoryFileSystem()
        fs.addContentToFile("/file.txt","line1")
        self.assertEqual("line1", fs.readContentFromFile("/file.txt"))
