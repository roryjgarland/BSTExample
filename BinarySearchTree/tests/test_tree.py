import unittest

from BinarySearchTree.tree import BST, Node


class TreeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = BST()

    def test_insert_method(self) -> None:
        self.tree.insert(14)

        self.assertIsInstance(self.tree.root, Node)
        self.assertEqual(14, self.tree.root.value)

    def test_find_method(self) -> None:
        self.tree.insert(14)
        self.tree.insert(5)
        self.tree.insert(23)
        self.tree.insert(9)
        self.tree.insert(32)

        value_in_tree = self.tree.find(23)
        self.assertIsInstance(value_in_tree, Node)
        self.assertEqual(value_in_tree.value, 23)

        self.assertIsNone(self.tree.find(43))
