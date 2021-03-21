import unittest

from BinarySearchTree.tree import BST, Node


class TreeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = BST()
        self.lst_un = [7, 5, 12, 3, 6, 8, 13, 4]
        self.lst_or = [1, 2, 3, 4, 5, 6, 7, 8]

    def test_insert_method(self) -> None:
        self.tree.insert(14)

        self.assertIsInstance(self.tree.root, Node)
        self.assertEqual(14, self.tree.root.value)

    def test_build_method_unordered_list(self) -> None:
        self.tree.build(self.lst_un)

        mid_un = len(self.lst_un) // 2
        root_val_un = self.lst_un[mid_un]

        self.assertIsInstance(self.tree.root, Node)
        self.assertEqual(self.tree.root.value, root_val_un)

    def test_build_method_ordered_list(self) -> None:

        self.tree.build(self.lst_or)

        mid_or = len(self.lst_or) // 2
        root_val_or = self.lst_or[mid_or]

        self.assertIsInstance(self.tree.root, Node)
        self.assertEqual(self.tree.root.value, root_val_or)

    def test_find_method(self) -> None:
        self.tree.build(self.lst_un)

        value_in_tree = self.tree.find(13)
        self.assertIsInstance(value_in_tree, Node)
        self.assertEqual(value_in_tree.value, 13)

        self.assertIsNone(self.tree.find(43))

    def test_height_method(self):
        self.tree.build(self.lst_un)

        height_tree = self.tree.height()

        self.assertEqual(height_tree, 4)

    def test_inorder_method(self) -> None:
        """
        Tree example
                    7
                5     12
              4  6   8  13
             3

        This should return: 3, 4, 5, 6, 7, 8, 12, 13

        :return:
        """

        result = [3, 4, 5, 6, 7, 8, 12, 13]

        self.tree.build(self.lst_un)

        tree_nodes = self.tree.dfs_walk()
        tree_nodes_v = [n.value for n in tree_nodes]

        self.assertListEqual(tree_nodes_v, result)

    def test_bfs_walk(self) -> None:
        """

                   7
                5     12
              4  6   8  13
            3

        This should return: 7, 5, 12, 4, 6, 8, 13, 3
        """

        result = [7, 5, 12, 4, 6, 8, 13, 3]

        self.tree.build(self.lst_un)

        tree_nodes = self.tree.bfs_walk()
        tree_nodes_v = [n.value for n in tree_nodes]

        self.assertListEqual(tree_nodes_v, result)
