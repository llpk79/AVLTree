from AVLTree import AVLTree
from random import randint
from timeit import default_timer as timer
from time import localtime as time



def child_height_diff(node):
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


def obeys_rules(node):
    if node.left and not node.right:
        return node.left.data < node.data
    if node.right and not node.left:
        return node.right.data > node.data
    if node.left and node.right:
        return node.left.data < node.data < node.right.data
    return True


def root_is_root(root):
    if root.parent:
        print('root not root!')
        print(root.data, root.parent.data)
    return not root.parent


def rules_and_balance(root, nodes):
    if root:
        rules_and_balance(root.left, nodes)
        rules = obeys_rules(root)
        balance = child_height_diff(root)
        if not rules and balance:
            # print(f'BST invariant compromised at {root.data}.')
            nodes += [root]
            nodes += ['Rules violated']
        elif not balance and rules:
            # print(f'Tree imbalanced at {root.data}.')
            print(root)
            nodes += [root]
            nodes += ['Tree imbalanced']
        elif not balance and not rules:
            # print(f'Tree all messed up at {root.data}.')
            print(root)
            nodes += [root]
            nodes += ['Tree all messed up']
        rules_and_balance(root.right, nodes)
    return nodes


def is_avl_tree(root):
    if not root:
        return True
    rnb = rules_and_balance(root, [])
    if not rnb and root_is_root(root):
        return True
    if rnb:
        with open('log.txt', 'a') as file:
            file.write(f'{time()}, \n{rnb[1]}\nAffected nodes: {rnb[0]}')
    return False


# Instantiate a tree.
tree = AVLTree()
print(is_avl_tree(tree.root))
print(len(tree))  # Tree size
print(tree.size)
print(tree)

# Add a value.
tree.insert(10)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Add a value smaller than root value.
tree.insert(7)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Add a value greater than root value.
tree.insert(13)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Add a value already in tree.
tree.insert(13)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Add a node to the left and right branches.
tree.insert(8)
tree.insert(11)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)


# Fill tree.
tree.insert(6)
tree.insert(14)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Delete a node with two children.
tree.delete(13)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)


# Delete a node with one child.
tree.delete(14)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Delete a leaf node.
tree.delete(6)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Delete a non-existent node.
tree.delete(6)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Delete root with two children.
tree.delete(10)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Delete root with one chile.
tree.delete(11)  # root.right
tree.delete(8)  # root
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)

# Delete last node.
tree.delete(7)
print(is_avl_tree(tree.root))
print(len(tree))
print(tree)




# Create tree for which insertion creates imbalance needing left rotation.
left = [3, 2]
for node in left:
    tree.insert(node)
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
for node in left_right:
    tree.insert(node)
print(is_avl_tree(tree.root))
print(tree)
# Insert value to cause imbalance.
tree.insert(15)
print(is_avl_tree(tree.root))
print(tree)

# Here the insertion is the left child of the root's predecessor.
tree.clear_tree()
for node in left_right:
    tree.insert(node)
tree.insert(8)
print(is_avl_tree(tree.root))
print(tree)


# Create tree for which insertion creates imbalance needing right rotation.
tree.clear_tree()
right = [1, 2]
for node in right:
    tree.insert(node)
print(is_avl_tree(tree.root))
print(tree)
tree.insert(3)
print(is_avl_tree(tree.root))
print(tree)

# Create tree for which insertion creates imbalance needing right then left rotations.
tree.clear_tree()
right_left = [4, 2, 10, 3, 6, 1, 11, 9, 8, 12]
for node in right_left:
    tree.insert(node)
print(is_avl_tree(tree.root))
print(tree)
tree.insert(5)
print(is_avl_tree(tree.root))
print(tree)
tree.clear_tree()
for node in right_left:
    tree.insert(node)
tree.insert(7)
print(is_avl_tree(tree.root))
print(tree)


# Inserting increasing values.
print('insert increasing')

tree.clear_tree()
for node in list(range(1000)):
    tree.insert(node)
print(is_avl_tree(tree.root))
print(tree.size)


# Insert decreasing values.
print('insert decreasing')

tree.clear_tree()
for node in list(range(1000, 0, -1)):
    tree.insert(node)
    is_avl_tree(tree.root)
print(is_avl_tree(tree.root))
print(tree.size)


# Insert random values.
print('insert random')

for node in range(10000):
    tree.insert(randint(-50000, 50000))
print(is_avl_tree(tree.root))
len_tree = len(tree)


# Delete some nodes.
print('delete some nodes.')

for node in range(2, 1000, 2):
    tree.delete(node)
print(is_avl_tree(tree.root))
print(len_tree - 499 == len(tree))


# Searching tree.
print('searching')

tree.clear_tree()
for node in list(range(15)):
    tree.insert(node)

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

for node in list(range(0, DATA_SIZE)):
    tree.insert(node)
print(is_avl_tree(tree.root))

arr = list(range(0, DATA_SIZE))

then = timer()
tree.search(1)
now = timer()
fast_low = now - then

then = timer()
search = 1 in arr
now = timer()
slow_low = now - then

print(slow_low / fast_low)

then = timer()
tree.search(50000)
now = timer()
fast_mid = now - then

then = timer()
search = 50000 in arr
now = timer()
slow_mid = now - then

print(slow_mid / fast_mid)

then = timer()
tree.search(999999)
now = timer()
fast_big = now - then

then = timer()
search = 999999 in arr
now = timer()
slow_big = now - then

print(slow_big / fast_big)
