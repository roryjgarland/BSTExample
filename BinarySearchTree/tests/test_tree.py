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
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(13)
        self.tree.insert(8)

        value_in_tree = self.tree.find(13)
        self.assertIsInstance(value_in_tree, Node)
        self.assertEqual(value_in_tree.value, 13)

        self.assertIsNone(self.tree.find(43))

    def test_height_method(self):
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(13)
        self.tree.insert(8)

        height_tree = self.tree.height()

        self.assertEqual(height_tree, 4)

    def test_inorder_method(self) -> None:
        """
        Tree example
                    7
                5     12
              3  6   8  13
               4

        This should return: 3, 4, 5, 6, 7, 8, 12, 13

        :return:
        """

        result = [3, 4, 5, 6, 7, 8, 12, 13]

        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(13)
        self.tree.insert(8)

        tree_nodes = self.tree.dfs_walk()
        tree_nodes_v = [n.value for n in tree_nodes]

        self.assertListEqual(tree_nodes_v, result)

    def test_bfs_walk(self) -> None:

        result = [7, 5, 12, 3, 6, 8, 13, 4]

        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(13)
        self.tree.insert(8)

        tree_nodes = self.tree.bfs_walk()
        tree_nodes_v = [n.value for n in tree_nodes]

        self.assertListEqual(tree_nodes_v, result)
