import unittest

from algkit.bits import *


class BitsTestCase(unittest.TestCase):

    def test_hamming_weight(self):
        self.assertEqual(3, hamming_weight(0b00000000000000000000000000001011))
        self.assertEqual(1, hamming_weight(0b00000000000000000000000010000000))
        self.assertEqual(31, hamming_weight(0b11111111111111111111111111111101))
        self.assertEqual(1, hamming_weight(0b00010000000000000000000000000000))


if __name__ == '__main__':
    unittest.main()
