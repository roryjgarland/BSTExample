from typing import Union


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


tree = BST()

tree.insert(5)
tree.insert(12)
tree.insert(2)
tree.insert(23)
tree.insert(3)

test = tree.find(23)
print(test.value)

