# AVLTree
Python AVL Tree module.

Tree designed for data types supporting <, =, >.

The following methods are implemented:
    
    Import module:
       from AVLTree import AVLTree

    Create a new tree:
        tree = AVLTree()

    View tree structure (may need some adjustment for screen size):
        print(tree)

    Determine height of tree:
        tree.height(print_result=True)
        Returns int
        print_result is optional, defaults to False

    Insert data into tree:
        tree.insert(data)
        If data already exists in tree, user is alerted

    Search for data in tree:
        tree.search(data, print_results=True)
        returns Boolean
        print_results is optional, defaults to False

    Delete data from tree:
        tree.delete(data)
        If data does not exist in tree, user is alerted

    Clear all data from tree:
        tree.clear_tree()
