class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

    def setdefault_child(self, char: str, default=None):
        return self.children.setdefault(char, default if default else TrieNode())

    def get_child(self, char: str):
        return self.children.get(char)


class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.node
        for char in word:
            node = node.setdefault_child(char)
        node.is_terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._find(word)
        return node is not None and node.is_terminal

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._find(prefix) is not None

    def _find(self, prefix: str):
        """Find the node that starts with the given prefix, or None when not found.
        :param str prefix:
        :return:
        """
        node = self.node
        for char in prefix:
            node = node.get_child(char)
            if node is None:
                return None
        return node
