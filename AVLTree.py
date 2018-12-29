from typing import TypeVar, Any, Iterable
"""AVLTree/Balanced Binary Search Tree Data structure.

Thanks for checking out my implementation of a BBST. Feel free to use it and/or change it to better suit your needs.
Any feedback is greatly appreciated.

"""

Q = TypeVar('Q', int, float, str)  # Q for qualitative.
Iq = Iterable[Q]  # Iterable/qualitative.


class Node(object):

    """Node object for AVLTree.

    Node class is wrapped by AVLTree class. All user methods are exposed there.
    Methods for printing, searching, inserting, deleting and determining height of AVLTree provided.

    """

    def __init__(self, data: Q)-> None:
        """Instantiates Node object for AVLTree.

        Data assumed to be compatible with <, =, > operators.

        Parent, left and right are pointers to parent and child nodes.

        Tallness initialized at 1, adjusted with insert and delete to represent height of node. Null nodes have
        height of 0.

        :param data: int, float, str.
        """
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.tallness = 1

    def __repr__(self)-> str:
        """Prints text representation of tree
        """
        if not self:
            return 'Tree is empty. Please insert data.'
        the_tree = '\n'
        nodes = [self]
        cur_tallness = self.tallness
        space = ' ' * (40 - int(len(str(self.data))) // 2)
        buffer = ' ' * (60 - int(len(str(self.data))) // 2)
        while True:
            if all(n is None for n in nodes):
                break
            cur_tallness -= 1
            this_row = ' '
            next_row = ' '
            next_nodes = []
            for cur_node in nodes:
                if not cur_node:
                    this_row += '           ' + space
                    next_nodes.extend([None, None])
                if cur_node and cur_node.data is not Node:
                    this_row += f'{buffer}{str(cur_node.data)}{buffer}'
                if cur_node and cur_node.left:
                    next_nodes.append(cur_node.left)
                    next_row += space + '/' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
                if cur_node and cur_node.right:
                    next_nodes.append(cur_node.right)
                    next_row += '\\' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
            the_tree += (cur_tallness * '   ' + this_row + '\n' + cur_tallness * '   ' + next_row + '\n')
            space = ' ' * int(len(space) // 2)
            buffer = ' ' * int(len(buffer) // 2)
            nodes = next_nodes
        return the_tree

    def print_tree(self, cur_node: 'Node', order: str=None)-> None:
        """Prints tree in specified order to stdout.

        :param cur_node: Root node from Tree.get_root.
        :param order: Keyword arg for order of tree traversal.
        """
        if order == 'pre-order':
            print(*self._pre_order(cur_node, []))
        elif order == 'in-order':
            print(*self._in_order(cur_node, []))
        elif order == 'post-order':
            print(*self._post_order(cur_node, []))

    def _pre_order(self, cur_node: 'Node', output: list)-> list:
        """Recursively traverses tree: Root -> Left node -> Right node.

        :param cur_node: Root of tree.
        :param output: Empty list.
        :return: List of node values.
        """
        if cur_node:
            output += [cur_node.data]
            self._pre_order(cur_node.left, output)
            self._pre_order(cur_node.right, output)
        return output

    def _in_order(self, cur_node: 'Node', output: list)-> list:
        """Recursively traverses tree: Left node -> Root -> Right node.

        :param cur_node: Node.Root of tree.
        :param output: Empty list.
        :return: List of node values.
        """
        if cur_node:
            self._in_order(cur_node.left, output)
            output += [cur_node.data]
            self._in_order(cur_node.right, output)
        return output

    def _post_order(self, cur_node: 'Node', output: list)-> list:
        """Recursively traverses tree: Left node -> Right node -> Root.

        :param cur_node: Root of tree.
        :param output: Empty list.
        :return: List of node values.
        """
        if cur_node:
            self._post_order(cur_node.left, output)
            self._post_order(cur_node.right, output)
            output += [cur_node.data]
        return output

    def height(self, cur_node: 'Node', cur_height: int)-> int:
        """Calculates and returns total height of tree.

        :param cur_node: Root of tree.
        :param cur_height:  0.
        :return: Height of tree.
        """
        if not cur_node:
            return cur_height
        left_height = self.height(cur_node.left, cur_height + 1)
        right_height = self.height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def search(self, cur_node: 'Node', data: Q)-> bool:
        """Searches tree for data, returns bool.

        :param cur_node: Root of tree.
        :param data: Data to be found in tree.
        :return: bool. True if data in tree, else, False.
        """
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left:
            return self.search(cur_node.left, data)
        elif data > cur_node.data and cur_node.right:
            return self.search(cur_node.right, data)
        return False

    def insert(self, cur_node: 'Node', data: Q, repeated_data: list)-> list:
        """Inserts data into tree. Alerts user if data already exists in tree.

        Calls _inspect_insertion to determine if insertion caused tree imbalance.

        :param cur_node: Root of tree.
        :param data: int, float, str.
        :param repeated_data: Empty list. Added to if data is already in the tree.
        """
        if data < cur_node.data:
            if not cur_node.left:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left, [])
            else:
                self.insert(cur_node.left, data, repeated_data)
            return repeated_data

        elif data > cur_node.data:
            if not cur_node.right:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right, [])
            else:
                self.insert(cur_node.right, data, repeated_data)
            return repeated_data

        # If many repeat values are expected and printing the occurrence is a nuisance,
        # toggle commenting on print statement.
        elif data == cur_node.data and cur_node.parent is not None:
            repeated_data += [1]
            # print(f'{data} already in tree. Cannot insert.')
            return repeated_data

    def _inspect_insertion(self, cur_node: 'Node', nodes: list)-> None:
        """ Determines if insertion creates need to balance sub-tree.

        Rebalance needed if difference in height of child nodes is > 1.
        Creates list of nodes to be rotated if above condition is true.
        Calls _rebalance_node with nodes to be balanced.

        :param cur_node: The newly inserted node.
        :param nodes: Empty list.
        :return:
        """
        if not cur_node.parent:
            return

        nodes = [cur_node] + nodes

        left = self._get_height(cur_node.parent.left)
        right = self._get_height(cur_node.parent.right)

        if abs(left - right) > 1 and len(nodes) > 1:
            nodes = [cur_node.parent] + nodes
            self._rebalance_node(*nodes[:3])
            return

        new = 1 + cur_node.tallness

        if new > cur_node.parent.tallness:
            cur_node.parent.tallness = new

        self._inspect_insertion(cur_node.parent, nodes)

    def _get_height(self, cur_node: 'Node')-> int:
        """ Gets height of cur_node. Returns 0 if node is None else returns node.tallness.

        :param cur_node: Node
        :return: Node.tallness
        """
        if not cur_node:
            return 0
        return cur_node.tallness

    def _rebalance_node(self, z: 'Node', y: 'Node', x: 'Node')-> None:
        """Determines orientation of imbalanced nodes and calls indicated balancing methods.

        Calls _rotate_right or _rotate_left as determined by orientation of unbalanced nodes.

        :param z: Highest node. Rebalance occurs 'around' this node.
        :param y: Child of z
        :param x: Child of y
        """
        if y == z.left and x == y.left:
            """    z
                  /
                 y
                /
               x   """
            self._right_rotate(z)

        elif y == z.left and x == y.right:
            """   z
                 /
                y 
                 \
                  x  """
            self._left_rotate(y)
            self._right_rotate(z)

        elif y == z.right and x == y.right:
            """   z
                   \
                     y 
                      \
                        x  """
            self._left_rotate(z)

        elif y == z.right and x == y.left:
            """   z
                    \
                      y
                    /
                  x  """
            self._right_rotate(y)
            self._left_rotate(z)

        else:
            raise Exception('Tree corrupted')

    def _right_rotate(self, z: 'Node')-> None:
        """Rotates around z to rebalance sub-tree.

        Makes z the right child of y.
        The parent of z becomes the parent of y.
        The right child of y becomes the right child of x.

        :param z: Root of sub-tree to be balanced.
        """
        temp = z.parent
        y = z.left
        x = y.right

        y.right = z
        z.parent = y
        z.left = x

        if x:
            x.parent = z

        y.parent = temp

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.tallness = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.tallness = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def _left_rotate(self, z: 'Node')-> None:
        """Rotates around z to rebalance sub-tree.

        Makes z the left child of y.
        The left child of y becomes the left child of x.

        :param z: Root of sub-tree to be balanced.
        """
        temp = z.parent
        y = z.right
        x = y.left

        y.left = z
        z.parent = y
        z.right = x

        if x:
            x.parent = z

        y.parent = temp

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.tallness = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.tallness = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def delete(self, node: 'Node')-> 'Node':
        """ Deletes node found in _find_node.

        Removes nodes and handles deleted node's orphaned children, if any.
        Deleted nodes with two children are handled by finding the smallest relative of the deleted node's right child,
        replacing the to-be-deleted node's data with that of its smaller relative, then marking the smaller relative
        to be deleted instead. This preserves the BST imperative.
        Calls _inspect_deletion to ensure proper balancing of sub-tree after deletion.


        :param node: Node to be deleted.
        :return: New root Node, if necessary.
        """

        def smallest_node(curr_node: 'Node')-> 'Node':
            """ Finds smallest relative of curr_node.

            :param curr_node: A Node.
            :return: Relative of curr_node with smallest value.
            """
            while curr_node.left:
                curr_node = curr_node.left
            return curr_node

        def children(curr_node: 'Node')-> int:
            """ Finds number of curr_node's children.

            :param curr_node: A node
            :return: Number of curr_node's children.
            """
            num = 0
            if curr_node.left:
                num += 1
            if curr_node.right:
                num += 1
            return num

        node_parent = node.parent
        node_children = children(node)

        # Leaf nodes may simply be deleted.
        if node_children == 0:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None

        # Parent of deleted node made parent of deleted node's child.
        if node_children == 1:
            if node.left:
                child = node.left
            else:
                child = node.right
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                child.parent = node_parent
                return child  # returned to promote child to root node
            child.parent = node_parent

        # If the node to be deleted has 2 children, the data of its next greater relative is promoted to the
        # to-be-deleted node. The relative is then deleted instead.
        if node_children == 2:
            successor = smallest_node(node.right)
            node.data = successor.data
            self.delete(successor)

        # Adjust height and inspect the tree for balance.
        if node_parent:
            node_parent.tallness = 1 + max(self._get_height(node_parent.left), self._get_height(node_parent.right))
            self._inspect_deletion(node_parent)

    def _inspect_deletion(self, cur_node: 'Node')-> None:
        """Ensures tree is balanced after deletion.

        Calls _rebalance_node if imbalance is detected.
        Calls _inspect_insertion to ensure balance up the tree.

        :param cur_node: Node. Parent of deleted node.
        :return:
        """
        if not cur_node:
            return

        left = self._get_height(cur_node.left)
        right = self._get_height(cur_node.right)

        if abs(left - right) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        if cur_node.parent:
            self._inspect_insertion(cur_node, [])

    def taller_child(self, cur_node: 'Node')-> 'Node':
        """Finds taller of node's children.

        :param cur_node: Node. Node to be inspected.
        :return: Node. Child of curr_node with greater height.
        """
        left = self._get_height(cur_node.left)
        right = self._get_height(cur_node.right)
        if left >= right:
            return cur_node.left
        return cur_node.right


class AVLTree(object):

    """Wraps Node class. Methods call corresponding methods of Node class.

    """

    def __init__(self)-> None:
        """Tree is represented by its root node, initially None.

        Tree designed for data types supporting <, =, >.

        The following methods are implemented:
            Create a new tree:
                tree = AVLTree()

            View tree structure (adjust for screen size):
                print(tree)

            Determine height of tree:
                tree.height(print_result=True)

                Returns int.

                Print_result is optional, defaults to False

            Insert data into tree:
                tree.insert(data)

                If data already exists in tree, user is alerted

            Search for data in tree:
                tree.search(data, print_results=True)

                Returns Boolean.

                Print_results is optional, defaults to False

            Delete data from tree:
                tree.delete(data)

                If data does not exist in tree, user is alerted

            Clear all data from tree:
                tree.clear_tree()

    """
        self.root = None
        self.size = 0

    def __repr__(self)-> str:
        """Prints text based structure of tree.

        :return: str. Tree structure.
        """
        if not self.root:
            return 'Tree is empty. Please insert data.'
        the_tree = '\n'
        nodes = [self._get_root()]
        cur_tallness = self.root.tallness
        space = ' ' * (40 - int(len(str(self.root.data))) // 2)
        buffer = ' ' * (60 - int(len(str(self.root.data))) // 2)
        while True:
            if all(n is None for n in nodes):
                break
            cur_tallness -= 1
            this_row = ' '
            next_row = ' '
            next_nodes = []
            for cur_node in nodes:
                if not cur_node:
                    this_row += '           ' + space
                    next_nodes.extend([None, None])
                if cur_node:
                    this_row += f'{buffer}{str(cur_node.data)}{buffer}'
                if cur_node and cur_node.left:
                    next_nodes.append(cur_node.left)
                    next_row += space + '/' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
                if cur_node and cur_node.right:
                    next_nodes.append(cur_node.right)
                    next_row += '\\' + space
                else:
                    next_nodes.append(None)
                    next_row += '       ' + space
            the_tree += (cur_tallness * '   ' + this_row + '\n' + cur_tallness * '   ' + next_row + '\n')
            space = ' ' * int(len(space) // 2)
            buffer = ' ' * int(len(buffer) // 2)
            nodes = next_nodes
        return the_tree

    def __len__(self)-> int:
        return self.size

    def _get_root(self, data: Q=None)-> 'Node':
        """Returns root node.

        Creates root node if called from Tree.insert and tree is empty.

        :param data: If provided and tree is empty, tree root is established with data.
        :return: Root node of tree.
        """
        if not self.root:
            if data is not None:
                self.root = Node(data)
                return self.root
            else:
                print('Tree is empty.')

        else:
            while self.root.parent:
                self.root = self.root.parent

        return self.root

    def print_tree(self, order: str=None)-> Any:
        """User interface for printing tree.

        Calls _print_tree with root from _get_root.
        Prints order as entered by user for correcting typos and such.
        Ensures print order requested is valid.

        :param order: 'in-order', 'pre-order', or 'post-order'
        :return: AVLTree._print_tree
        """
        print(order)
        if not order or not any([order == 'pre-order', order == 'post-order', order == 'in-order']):
            print('Please specify a valid print order.')
            print('(eg. order=\'in-order\', \'pre-order\', or \'post-order\')')
        return self._print_tree(self._get_root(), order)

    def _print_tree(self, root: 'Node', order: str=None)-> Any:
        """Calls print_tree method of Node class.

        :param root: Root node
        :param order: 'in-order', 'pre-order', or 'post-order'
        :return: Node.print_tree
        """
        return root.print_tree(root, order)

    def height(self, print_result: bool=False)-> int:
        """User interface for finding height of tree.

        Calls _height with root from _get_root.
        Option to print height to stdout.

        :param print_result: Prints height to stdout if True.
        :return: _height
        """
        height = self._height(self._get_root())
        if print_result:
            print(height)
        return height

    def _height(self, root: 'Node')-> Any:
        """Calls height method of Node class.

        :param root: Root node.
        :return: Node.height
        """
        return root.height(root, 0)

    def search(self, data: Q, print_result: bool=False)-> bool:
        """User interface for search method.

        Calls _search with root from _get_root.
        Option to print results to stdout.

        :param print_result: Set to True to print search results.
        :param data: Data to be found in tree.
        :return: AVLTree._search
        """
        result = self._search(self._get_root(), data)

        if print_result:
            if result:
                print(f'{data} found.')
            else:
                print(f'{data} not found.')

        return result

    def _search(self, root: 'Node', data: Q)-> Any:
        """Calls search method of Node class.

        :param root: Root node.
        :param data: Data to search for in tree.
        :return: Node.search
        """
        return root.search(root, data)

    def insert(self, data: Q or Iq)-> None:
        """User interface for inserting data into tree.

        Calls _insert with root provided by _get_root.
        Resets root after insert in case rotation changes root.
        Data field provided to _get_root ensures tree root is created on first insertion.

        :param data: int, float, str or Iterable[int, float, str].
        """
        if isinstance(data, Iterable):
            for x in data:
                result = self._insert(self._get_root(data=x), x)
                if not result:
                    self.size += 1
                self.root = self._get_root()
        else:
            result = self._insert(self._get_root(data=data), data)
            if not result:
                self.size += 1
            self.root = self._get_root()

    def _insert(self, root: 'Node', data: Q)-> Any:
        """Calls insert method of Node class.

        :param root: Root node.
        :param data: Data to be inserted into tree.
        :return: Node.insert
        """
        return root.insert(root, data, [])

    def _find_node(self, cur_node: 'Node', data: Q)-> Any:
        """Finds and returns node with given data, else, returns None.

        :param cur_node: Root node from _get_root.
        :param data: Data contained within node to be found.
        :return: Node containing data if such a node exists, else, None.
        """
        if cur_node and data == cur_node.data:
            return cur_node
        elif cur_node and data < cur_node.data:
            return self._find_node(cur_node.left, data)
        elif cur_node and data > cur_node.data:
            return self._find_node(cur_node.right, data)
        return None

    def delete(self, data: Q)-> None:
        """Passes root and data to be deleted to _delete.

        Calls _delete with root from _get_root.

        :param data: Data to delete from tree.
        :return: _delete if data in tree, else, None.
        """
        node = self._find_node(self._get_root(), data)

        if not node:
            print(f'{data} not in tree, Cannot delete.')
            return

        self.size -= 1
        self._delete(node)
        self.root = self._get_root()

    def _delete(self, node: 'Node')-> None:
        """Calls delete method of Node class.

        If root is to be deleted and has no children, root is set to None.
        If Node.delete returns a node it is the new root node.

        :param node: Node to be deleted
        """
        if node == self.root and (not node.left and not node.right):
            self.clear_tree()

        result = node.delete(node)
        if result:
            self.root = result

        self.root = self._get_root()

    def clear_tree(self)-> None:
        """Clears tree of all data.

        :return: Tree root
        """
        self.root = None
        self.size = 0
