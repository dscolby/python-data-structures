"""This module contains an implementation of a red black tree.
"""
from typing import Union, Any

class RedBlackTree:
    """A red black tree implementation that accepts multiple types of  keys.
    """
    
    class Node:
        """A red black tree node implementation.

        Attributes:
            key: The key.
            value: The value associated with the key.
            left: The left child, if it exists.
            right: The right child, if it exists.
            parent: The node's parent, if it exists.
            color: Whether the node is red or black.
        """
        def __init__(self, key: Union[int, float]=None, value: Any=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.color = 'R'

    def __init__(self):
        """Initialize a red black tree.

        Args:
            tree: The red black tree.
        """
        self.tree = self.Node()
        self.tree.color = 'R'

    def insert(self, key: Union[int, float], value: Any) -> None:
        """Insert a value into the tree.

        If a key already exists, then its value is updated with the new value.

        Args:
            key: The key of the item to insert.
            value: The item to insert.
        """
        # If there's already a key, then we look in the current node and go down
        # a level if it's not the one we're looking for
        if self.tree.key:

            # If the key we're looking for is smaller than the current one, then we
            # search the left node and repeat the process until there is no new node
            if key < self.tree.key:
                if not self.tree.left:
                    self.tree.left = self.Node(key, value)
                    self.tree.left.parent = self.tree
                else:
                    self.insert(key, value)

            # If the key we're looking for is larger than the current one, then we
            # search the right node and repeat the process until there is no new node
            if key > self.tree.key:
                if not self.tree.right:
                    self.tree.right = self.Node(key, value)
                    self.tree.right.parent = self.tree
                else:
                    self.tree.right.insert(key, value)

            # Updating the value if the key already exists
            if key == self.tree.key:
                self.tree.value = value

        # If there's no key, then we're at the top and we just add the key and value
        else:
            self.tree.key = key
            self.tree.value = value

    def fix_insert(self, node: Node) -> None:
        """Rebalance the tree.

        Args:
            node: the node to start at.
        """
        while node.parent and node.parent.color == 'R':

            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left

                if uncle.color == 'R':
                    uncle.color = 'B'
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent

                else:

                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.left_rotate(node.parent.parent)

            else:
                uncle = node.parent.parent.right

                if uncle.color == 'R':
                    uncle.color = 'B'
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent

                else:

                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.right_rotate(node.parent.parent)

            if node == self.tree:
                break

        self.tree.color = 'B'

    def left_rotate(self, node: Node) -> None:
        """Left rotate a node to enforce the red balck properties

        Args:
            node: The node to rotate.
        """
        sibling = node.right
        node.right = sibling.left

        if sibling.left != self.tree:
            sibling.left.parent = node

        sibling.parent = node.parent

        if not node.parent:
            self.tree = sibling

        elif node == node.parent.left:
            node.parent.left = sibling

        else:
            node.parent.right = sibling

        sibling.left = node
        node.parent = sibling

    def right_rotate(self, node: Node) -> None:
        """Right a node to enforce the red balck properties.

        Args:
            node: The node to rotate.
        """
        sibling = node.left
        node.left = sibling.right

        if sibling.right != self.tree:
            sibling.right.parent = node

        sibling.parent = node.parent

        if not node.parent:
            self.tree = sibling

        elif node == node.parent.right:
            node.parent.right = sibling

        else:
            node.parent.left = sibling

        sibling.right = node
        node.parent = sibling
