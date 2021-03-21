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
    """
    Class which constructs a binary search tree. There are two ways to add data to this

    bst = BST()
    bst.insert(7)  # First value is always the insert value
    bst.insert(5)
    bst.insert(12)

    OR

    bst = BST()
    bst.build([7, 5, 12])  # this list does not have to be ordered


    """
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
        :param x: type(int) value we are looking for
        :return:
        """

        if self.root is None:
            return None
        else:
            return self._find(x, self.root)

    def _find(self, x: int, c_node: Node) -> Union[None, Node]:
        """
        Recursive function of _find
        :param x: type(int) value we are looking for
        :param c_node: type(Node) current node
        :return:
        """

        if x == c_node.value:
            return c_node
        elif x < c_node.value and c_node.l_child:
            return self._find(x, c_node.l_child)
        elif x > c_node.value and c_node.r_child:
            return self._find(x, c_node.r_child)
        else:
            return None

    def height(self) -> int:
        """
        Function which returns the height (# levels) of the tree
        """

        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, c_node: Node, c_height: int) -> int:
        """
        Recursive function for height which goes through each node
        :param c_node: type(Node) current node
        :param c_height: type(int) current height of tree
        """
        if c_node is None:
            return c_height

        l_height = self._height(c_node.l_child, c_height + 1)
        r_height = self._height(c_node.r_child, c_height + 1)
        return max(l_height, r_height)

    def dfs_walk(self) -> Union[None, List[Node]]:
        """
        Use stack here: LIFO as we want to go to the deepest value first

        This performs an inorder traversal method of the tree i.e. left - visit - right:

                   7
                5     12
              4  6   8  13
             3

        This should return: 3, 4, 5, 6, 7, 8, 12, 13 (i.e. in order)

        :return:
        """

        inorder_l = []

        if self.root is None:
            return None
        else:
            return self._dfs_walk(self.root, inorder_l)

    def _dfs_walk(self, c_node: Node, inorder_l: List[Node]) -> List[Node]:
        """
        :param c_node: type(Node) current node
        :inorder_l: type(List[Node])) list of Nodes in order of depth
        """

        if c_node is not None:
            self._dfs_walk(c_node.l_child, inorder_l)
            inorder_l.append(c_node)
            self._dfs_walk(c_node.r_child, inorder_l)

        return inorder_l

    def bfs_walk(self):
        """
        Breadth width search. We use a queue here: FIFO

                   7
                5     12
              4  6   8  13
            3

        This should return: 7, 5, 12, 4, 6, 8, 13, 3

        """

        visited_l = []
        queue_l = []

        if self.root is None:
            return None

        else:
            queue_l.append(self.root)

            while queue_l:
                s = queue_l.pop(0)
                visited_l.append(s)

                if s.l_child is not None:
                    queue_l.append(s.l_child)
                if s.r_child is not None:
                    queue_l.append(s.r_child)

        return visited_l

    def build(self, lst: List[int]):
        """
        This function builds a BST from a list, tries to make the tree balanced by splitting the list in half.

        :param lst: type(list) list that builds binary tree. Can be unordered
        """

        # finding the middle value to be our root

        if self.root is None:
            # sorting the list
            lst.sort()
            # getting middle value
            mid = len(lst) // 2

            # setting the root
            self.insert(lst[mid])

            # updating the tree
            self._build(lst[:mid], self.root)
            self._build(lst[mid+1:], self.root)

        else:
            print('Tree already built from list, use insert!')

    def _build(self, lst: List[int], c_node: Node):
        """
        Function which builds a balanced tree from a list

        :param lst: type(list[int]) list of integere values
        :param c_node: type(Node) current node being looked at

        """
        if not lst:
            return None

        mid = len(lst) // 2

        self.insert(lst[mid])

        self._build(lst[:mid], c_node)
        self._build(lst[mid + 1:], c_node)
