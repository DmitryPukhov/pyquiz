from typing import Dict


class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

    Example:

    Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
    [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

    Constraints:
    1 <= word.length <= 500
    word in addWord consists lower-case English letters.
    word in search consist of  '.' or lower-case English letters.
    At most 50000 calls will be made to addWord and search.
    """

    class TrieNode:
        def __init__(self, val: str):
            self.val = val
            self.children = dict()
            self.endmark = False

        def __str__(self):
            return self.val

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = self.TrieNode(None)

    def addWord(self, word: str) -> None:
        node = self.trie
        # For each letter in the word add it to the trie level if does not already exist
        for letter in word:
            if letter not in node.children:
                # Add a new letter to the trie
                node.children[letter] = self.TrieNode(letter)
            # Go to next level in the trie
            node = node.children[letter]
        # Set end mark
        node.endmark = True

    def search(self, word: str) -> bool:
        """Recursive search the first letter in the word"""
        out = self.searchNode(word, self.trie)
        return out

    def searchNode(self, word: str, node: TrieNode) -> bool:
        """
        Recursive search first letter of the word in the node
        """
        if not word:
            # End of word reached, all letters were in trie
            return node.endmark
        letter = word[0]
        if letter == '.':
            for child in node.children.values():
                if self.searchNode(word[1:], child):
                    return True
            return False
        elif letter in node.children:
            return self.searchNode(word[1:], node.children[letter])
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
