import unittest

from algkit import binarytree


class BinaryTreeTestCase(unittest.TestCase):

    def test_preorder(self):
        self.assertEqual([], binarytree.preorder(None))

        root = binarytree.build("[1,null,2,3]")
        self.assertEqual([1, 2, 3], binarytree.preorder(root))


if __name__ == '__main__':
    unittest.main()
