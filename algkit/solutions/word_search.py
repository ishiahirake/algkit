from typing import List

from toolkit import is_between
from trie import Trie


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Given a 2D board and a list of words from the dictionary, find all words in the board.

    :see https://leetcode.com/problems/word-search-ii/

    :param board:
    :param words:
    :return:
    """
    if not board or not words:
        return []

    trie = Trie()
    for word in words:
        trie.insert(word)

    exists = set()

    row, col = len(board), len(board[0])
    for ri in range(row):
        for ci in range(col):
            _dfs(board, ri, ci, '', trie, exists)

    return list(exists)


def _dfs(board: List[List[str]], ri: int, ci: int, word: str, trie: Trie, exists):
    row, col = len(board), len(board[0])
    if not is_between(ri, 0, row - 1) or not is_between(ci, 0, col - 1):
        return

    char = board[ri][ci]
    if char == '#':
        return

    word = word + char

    if not trie.starts_with(word):
        return

    if trie.search(word):
        exists.add(word)

    board[ri][ci] = '#'

    _dfs(board, ri - 1, ci, word, trie, exists)
    _dfs(board, ri + 1, ci, word, trie, exists)
    _dfs(board, ri, ci - 1, word, trie, exists)
    _dfs(board, ri, ci + 1, word, trie, exists)

    board[ri][ci] = char


def exist_word(board: List[List[str]], word) -> bool:
    """
    Given a 2D board and a word, find if the word exists in the grid.

    A simple solution by using find_words.

    :see https://leetcode.com/problems/word-search/

    :param board:
    :param word:
    :return:
    """
    return len(find_words(board, [word])) != 0
