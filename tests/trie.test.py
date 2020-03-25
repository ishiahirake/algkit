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

    def test_pattern_search(self):
        wd = Trie()
        wd.insert("bad")
        wd.insert("dad")
        wd.insert("mad")

        self.assertFalse(wd.pattern_search("pad"))
        self.assertTrue(wd.pattern_search("bad"))
        self.assertTrue(wd.pattern_search(".ad"))
        self.assertTrue(wd.pattern_search("b.."))


if __name__ == '__main__':
    unittest.main()
