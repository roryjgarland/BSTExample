class Node:
    """
    Represents our node object and contains on the value of a given node and its left/right children
    """

    def __init__(self, value):
        self.value = value
        self.l_child = None
        self.r_child = None


class BST:
    def __init__(self):
        self.root = None
