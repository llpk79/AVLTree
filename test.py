from AVLTree import AVLTree, Node
from random import randint
from timeit import default_timer as timer
from time import localtime as time


def node_is_balanced(node: Node)-> bool:
    """Checks balance of node by finding difference in height between children of node.

    Returns True if difference is > 1 else False

    :param node: A Node.
    :return: bool
    """
    if not node.left:
        left = 0
    else:
        left = node.left.tallness
    if not node.right:
        right = 0
    else:
        right = node.right.tallness
    if abs(left - right) > 1:
        return False
    return True


def obeys_rules(node: Node)-> bool:
    """Checks that BST invariant is obeyed at this node.

    Data to the left must be < node.data.
    Data to the right must be > node.data.
    Returns True if above conditions hold, else False.

    :param node: A Node.
    :return: bool
    """
    if node.left and not node.right:
        return node.left.data < node.data
    if node.right and not node.left:
        return node.right.data > node.data
    if node.left and node.right:
        return node.left.data < node.data < node.right.data
    return True


def root_is_root(root: Node)-> bool:
    """Checks if root node has a parent.

    Returns True if no parent found, else False

    :param root: A Node
    :return: bool
    """
    if root.parent:
        print('Root not root!')
        print(root.data, root.parent.data)
    return not root.parent


def rules_and_balance(root: Node, bad_nodes: list)-> list:
    """Recursively checks that tree is balanced and follows BST rules.

    If either are violated, adds affected nodes and type of violation to bad_nodes.
    Returns list of violations and affected nodes.

    :param root: Root Node.
    :param bad_nodes: Empty list
    :return: list
    """
    if root:
        rules_and_balance(root.left, bad_nodes)
        rules = obeys_rules(root)
        balanced = node_is_balanced(root)
        if not rules and balanced:
            bad_nodes += [root]
            bad_nodes += ['Rules violated']
        elif not balanced and rules:
            print(root)
            bad_nodes += [root]
            bad_nodes += ['Tree imbalanced']
        elif not balanced and not rules:
            print(root)
            bad_nodes += [root]
            bad_nodes += ['Tree all messed up']
        rules_and_balance(root.right, bad_nodes)
    return bad_nodes


def is_avl_tree(root: Node)-> bool:
    """Checks validity of root, tree balance, and BST invariant.

    If any violations are found, adds affected node and type of violation to log file with time-stamp.
    Returns True if all AVL tree conditions are met, else False.

    :param root: Root Node.
    :return: bool
    """
    if not root:
        return True
    rnb = rules_and_balance(root, [])
    true_root = root_is_root(root)
    if not rnb and true_root:
        return True
    if rnb:
        with open('log.txt', 'a') as file:
            file.write(f'{time()}, \n{rnb[1]}\nAffected nodes: {rnb[0]}')
    if not true_root:
        with open('log.txt', 'a') as file:
            file.write(f'{time()}, \nAffected node: {root}')
    return False


# Okay, let's do some testing!

# Instantiate a tree.
tree = AVLTree()
print(is_avl_tree(tree.root))
print(len(tree))  # Tree size
print(tree.size)
print(tree)

# Add a value.
tree.insert(10)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Add a value smaller than root value.
tree.insert(7)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Add a value greater than root value.
tree.insert(13)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Add a value already in tree.
tree.insert(13)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Add a node to the left and right branches.
tree.insert(8)
tree.insert(11)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)


# Fill tree.
tree.insert(6)
tree.insert(14)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Delete a node with two children.
tree.delete(13)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)


# Delete a node with one child.
tree.delete(14)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Delete a leaf node.
tree.delete(6)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Delete a non-existent node.
tree.delete(6)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Delete root with two children.
tree.delete(10)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Delete root with one chile.
tree.delete(11)  # root.right
tree.delete(8)  # root
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Delete last node.
tree.delete(7)
print(is_avl_tree(tree.root))
print(tree.size)
print(tree)

# Create tree for which insertion creates imbalance needing left rotation.
left_data = [3, 2]
for data in left_data:
    tree.insert(data)
print(is_avl_tree(tree.root))
print(tree)
tree.insert(1)
print(is_avl_tree(tree.root))
print(tree)


# Clear the tree.
tree.clear_tree()
print(is_avl_tree(tree.root))
print(tree)


# Create tree for which insertion creates imbalance needing left then right rotations.
# Here the insertion is the right child of the root's predecessor.

left_right = [20, 4, 26, 3, 9, 21, 30, 2, 7, 11]
for data in left_right:
    tree.insert(data)
print(is_avl_tree(tree.root))
print(tree)

# Insert value to cause imbalance.
tree.insert(15)
print(is_avl_tree(tree.root))
print(tree)

# Here the insertion is the left child of the root's predecessor.
tree.clear_tree()
for data in left_right:
    tree.insert(data)
tree.insert(8)
print(is_avl_tree(tree.root))
print(tree)


# Create tree for which insertion creates imbalance needing right rotation.
tree.clear_tree()
right_data = [1, 2]
for data in right_data:
    tree.insert(data)
print(is_avl_tree(tree.root))
print(tree)
tree.insert(3)
print(is_avl_tree(tree.root))
print(tree)

# Create tree for which insertion creates imbalance needing right then left rotations.
tree.clear_tree()
right_left = [4, 2, 10, 3, 6, 1, 11, 9, 8, 12]
for data in right_left:
    tree.insert(data)
print(is_avl_tree(tree.root))
print(tree)
tree.insert(5)
print(is_avl_tree(tree.root))
print(tree)
tree.clear_tree()
for data in right_left:
    tree.insert(data)
tree.insert(7)
print(is_avl_tree(tree.root))
print(tree)


# Inserting increasing values.
print('insert increasing')
tree.clear_tree()
for data in list(range(1000)):
    tree.insert(data)
print(is_avl_tree(tree.root))
print(tree.size)


# Insert decreasing values.
print('insert decreasing')
tree.clear_tree()
for data in list(range(1000, 0, -1)):
    tree.insert(data)
    is_avl_tree(tree.root)
print(is_avl_tree(tree.root))
print(tree.size)


# Insert random values.
print('insert random')
for _ in range(10000):
    tree.insert(randint(-50000, 50000))
print(is_avl_tree(tree.root))
len_tree = len(tree)


# Delete some nodes.
print('delete some nodes.')
for data in range(2, 1000, 2):
    tree.delete(data)
print(is_avl_tree(tree.root))
print(len_tree - 499 == len(tree))


# Searching tree.
print('searching')
tree.clear_tree()
for data in list(range(15)):
    tree.insert(data)

print(tree.search(2))
print(tree.search(22))
tree.search(2, print_result=True)
tree.search(22, print_result=True)


# Tree height.
print(tree.height())
tree.height(print_result=True)

tree.clear_tree()


# Checking lookup speed.

DATA_SIZE = 100000

for data in list(range(0, DATA_SIZE)):
    tree.insert(data)
print(is_avl_tree(tree.root))

arr = list(range(0, DATA_SIZE))

then = timer()
tree.search(1)
now = timer()
fast_low = now - then

then = timer()
mini_search = 1 in arr
now = timer()
slow_low = now - then

print(slow_low / fast_low)

then = timer()
tree.search(50000)
now = timer()
fast_mid = now - then

then = timer()
med_search = 50000 in arr
now = timer()
slow_mid = now - then

print(slow_mid / fast_mid)

then = timer()
tree.search(999999)
now = timer()
fast_big = now - then

then = timer()
long_search = 999999 in arr
now = timer()
slow_big = now - then

print(slow_big / fast_big)
