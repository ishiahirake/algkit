import unittest

from algkit.solutions import find_words, exist_word


class WordSearchTestCase(unittest.TestCase):

    def test_find_words_n1(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        words = ["oath", "pea", "eat", "rain"]
        self.assert_find_words(board, words, ["eat", "oath"])

    def test_find_words_e1(self):
        self.assert_find_words(
            board=[["a", "a"]],
            words=["a"],
            excepted=["a"]
        )

    def assert_find_words(self, board, words, excepted):
        self.assertEqual(sorted(excepted), sorted(find_words(board, words)))

    def test_exist_word(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]

        self.assertTrue(exist_word(board, 'ABCCED'))
        self.assertTrue(exist_word(board, 'SEE'))
        self.assertFalse(exist_word(board, 'ABCB'))


if __name__ == '__main__':
    unittest.main()
