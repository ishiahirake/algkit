import unittest

from algkit.trie import Trie


class TrieTestCase(unittest.TestCase):

    def test_search(self):
        trie = Trie()
        self.assertFalse(trie.search('Apple'))
        trie.insert('Apple')
        self.assertTrue(trie.search('Apple'))
        self.assertFalse(trie.search('App'))

    def test_starts_with(self):
        trie = Trie()
        self.assertFalse(trie.starts_with('App'))
        trie.insert('Apple')
        self.assertTrue(trie.starts_with('App'))


if __name__ == '__main__':
    unittest.main()
