from typing import Union, List


class Node:
    """
    Represents our node object and contains on the value of a given node and its left/right children
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.l_child = None
        self.r_child = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        """
        Outward facing insert value which inserts a new node into our tree. Checks if the root exists, if not generates
        node otherwise calls the "private" function
        :param value:
        :return:
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, c_node: Node) -> None:
        """
        Recursive nature of insert is described here, checking to see if the node has either a left or right child
        depending on the value
        :param value:
        :param c_node:
        :return:
        """

        if c_node.value > value:
            if c_node.l_child is None:
                c_node.l_child = Node(value)
            else:
                self._insert(value, c_node.l_child)

        elif c_node.value < value:
            if c_node.r_child is None:
                c_node.r_child = Node(value)
            else:
                self._insert(value, c_node.r_child)
        else:
            print(f'You cannot have the same value twice, current_node: {c_node.value}, value: {value}!')

    def find(self, x: int) -> Union[None, Node]:
        """
        Function which finds a certain node
        :param x:
        :return:
        """

        if self.root is None:
            return None
        else:
            return self._find(x, self.root)

    def _find(self, x: int, c_node: Node) -> Union[None, Node]:

        if x == c_node.value:
            return c_node
        elif x < c_node.value and c_node.l_child:
            return self._find(x, c_node.l_child)
        elif x > c_node.value and c_node.r_child:
            return self._find(x, c_node.r_child)
        else:
            return None

    def dfs_walk(self) -> Union[None, List[int]]:
        """
        This performs an inorder traversal method of the tree i.e. left - visit - right:

                   7
                5     12
              3  6   8  13
               4

        This should return: 3, 4, 5, 6, 7, 8, 12, 13 (i.e. in order)

        :return:
        """

        inorder_l = []

        if self.root is None:
            return None
        else:
            return self._dfs_walk(self.root, inorder_l)

    def _dfs_walk(self, c_node: Node, inorder_l) -> List[int]:

        if c_node is not None:
            self._dfs_walk(c_node.l_child, inorder_l)
            inorder_l.append(c_node)
            self._dfs_walk(c_node.r_child, inorder_l)

        return inorder_l
