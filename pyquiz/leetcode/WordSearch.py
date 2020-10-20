from typing import List


class WordSearch:
    """
    Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells,
    where "adjacent" cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.


    Example 1:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]],
            word = "ABCCED"
    Output: true

    Example 2:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]],
            word = "SEE"
    Output: true

    Example 3:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]],
            word = "ABCB"
    Output: false

    Constraints:
    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False

        # Try to start dfs from each cell with the first letter of the word
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col][0] == word[0]:
                    # Start DFS
                    ht = set()
                    if self.dfs(board, word, row, col, ht):
                        return True

        return False

    def dfs(self, board: List[List[str]], word: str, row, col, ht):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            # We moved out of board
            return False
        if (row, col) in ht:
            # Already used this letter
            return False
        if len(word) == 1:
            # End of search branch in the tree
            ht.add((row, col))
            return board[row][col][0] == word[0]
        if board[row][col] != word[0]:
            # Current cell is not required word letter, stop search
            return False
        # Current cell == word[0], mark the cell as visited and continue dfs
        ht.add((row, col))
        return self.dfs(board, word[1:], row, col + 1, ht.copy()) or \
               self.dfs(board, word[1:], row + 1, col, ht.copy()) or \
               self.dfs(board, word[1:], row, col - 1, ht.copy()) or \
               self.dfs(board, word[1:], row - 1, col, ht.copy())
