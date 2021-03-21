from BinarySearchTree.tree import BST
import random

if __name__ == '__main__':

    lst = random.sample(range(1, 13), 6)
    bst = BST()
    bst.build(lst)

    print(f'The root is {bst.root.value}')

    dfs_walk = bst.dfs_walk()
    print('DFS walk', [n.value for n in dfs_walk])

    bfs_walk = bst.bfs_walk()
    print('BFS walk', [n.value for n in bfs_walk])
