# -*- coding: utf8 -*-
import unittest
from main import *


class TestPyHuff(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")

    def test_make_huffman_code_1(self):
        """make_huffman_code test #1"""
        node_left = Node("a", None)
        node_right = Node("b", None)
        node_root = Node(node_left, node_right)
        self.assertEqual(make_huffman_code(node_root),
                         {'a': '00', 'b': '10'})

    def test_make_huffman_code_2(self):
        """make_huffman_code test #2"""
        node_root = Node(None, None)
        self.assertEqual(make_huffman_code(node_root),
                         {})

    def test_make_tree_1(self):
        """make_tree test #1"""
        l = [("a", 5), ("b", 1)]
        l = make_tree(l)
        self.assertEqual(type(l),
                         Node)

    def test_make_tree_2(self):
        """make_tree test #2"""
        l = [("a", 5), ("b", 1)]
        l = make_tree(l)
        self.assertEqual(l.get_leaves(),
                         ('b', 'a'))

    def test_count_symbols_and_frequency(self):
        """count_symbols_and_frequency test"""
        self.assertEqual(count_symbols_and_frequency("test_txts/"),
                         {'a': 20, 'b': 16, 'c': 12, 'd': 8, ' ': 4})


if __name__ == '__main__':
    unittest.main(exit=False)
