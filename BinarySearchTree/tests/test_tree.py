import unittest
from BinarySearchTree.tree import BST, Node

class TreeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = BST()

    def test_find_method(self) -> None:
        self.tree.insert(14)
        self.tree.insert(5)
        self.tree.insert(23)
        self.tree.insert(9)
        self.tree.insert(32)

        self.assertIsInstance(self.tree.find(23), Node)
        self.assertIsNone(self.tree.find(43))
