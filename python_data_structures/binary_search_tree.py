"""This module contains an implementation fo a binary search tree.
"""
from typing import Any, Union

class BinarySearchTree:
    """A simple binary search tree.

    Attributes:
        left: The left node
        right: The right node.
        key: The key.
        value: The vlaue associated with the key.
    """
    def __init__(self, key: Union[int, float, str, tuple]=None, value: Any=None) -> None:
        """Initialize a binary search tree.

        Args:
            left: The node's left child, if it exists.
            right: The node's right child, if it exists.
            key: The key to use.
            value: The value associated with the key.
        """
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def put(self, key: Union[int, float, str, tuple], value: Any) -> None:
        """Put a key and value into the tree.

        Args:
            key: The key to use.
            value: The value corresponding to the key.
        """
        # We're not actually doing anything here, just dispatching based on they key type
        if isinstance(key, (float, int)):
            self.insert(key, value)
        elif isinstance(key, str):
            new_key = self.string_to_number(key)
            self.insert(new_key, value)
        elif isinstance(key, tuple):
            new_key = self.tuple_to_number(key)
            self.insert(new_key, value)
        else:
            raise KeyError("Keys must be hashable")

    def insert(self, key: Union[int, float], value: Any) -> None:
        """Insert a value into the tree.

        If a key already exists, then its value is updated with the new value.

        Args:
            key: The key of the item to insert.
            value: The item to insert
        """
        # If there's already a key, then we look in the current node and go down
        # a level if it's not the one we're looking for
        if self.key:

            # If the key we're looking for is smaller than the current one, then we
            # search the left node and repeat the process until there is no new node
            if key < self.key:
                if self.left is None:
                    self.left = BinarySearchTree(key, value)
                else:
                    self.left.insert(key, value)

            # If the key we're looking for is larger than the current one, then we
            # search the right node and repeat the process until there is no new node
            if key > self.key:
                if self.right is None:
                    self.right = BinarySearchTree(key, value)
                else:
                    self.right.insert(key, value)

            if key == self.key:
                self.value = value

        # if there's no key, then we're at the top and we just add the key and value
        else:
            self.key = key
            self.value = value

    def find(self, key: Union[int, float, str, tuple]) -> None:
        """Find the value associated with a given key, if it exists.

        Args:
            key: The key to use.

        Returns:
            The value associated with the given key
        """
        # We're not actually doing anything here, just dispatching based on they key type
        if isinstance(key, (float, int)):
            return self.retrieve(key)
        elif isinstance(key, str):
            new_key = self.string_to_number(key)
            return self.retrieve(new_key)
        elif isinstance(key, tuple):
            new_key = self.tuple_to_number(key)
            return self.retrieve(new_key)
        else:
            raise KeyError("Keys must be hashable")

    def retrieve(self, key: Union[int, float, str, tuple]) -> Any:
        """Retrieve the value that corresponds to a given key.

        Args:
            key: The key to use

        Returns:
            The value corresponding to the key if it exists in the tree.
        """
        # If there is a key then we can keep searching
        if self.key:

            # If the key in the node is the one we're looking for then we return its value
            if self.key == key:
                return self.value

            # If the key we're looking for is smaller, then we search the left child
            # and return it's value or search its children
            if key < self.key and self.left:
                return self.left.retrieve(key)

            # If the key we're looking for is larger, then we search the right child
            # and return it's value or search its children
            if key > self.key and self.right:
                return self.right.retrieve(key)

        # If there's no key in a node then we've reached the end and not found the node
        return None

    def delete(self, key: Union[int, float, str, tuple]) -> Any:
        """Delete the value associated with a given key, if it exists.

        Args:
            key: The key to use.

        Returns:
            The value associated with the given key
        """
        # We're not actually doing anything here, just dispatching based on they key type
        if isinstance(key, (float, int)):
            self.delete_node(key)
        elif isinstance(key, str):
            new_key = self.string_to_number(key)
            self.delete_node(new_key)
        elif isinstance(key, tuple):
            new_key = self.tuple_to_number(key)
            self.delete_node(new_key)
        else:
            raise KeyError("Keys must be hashable")

    def delete_node(self, key: Union[int, float]):
        """Delete a node with the given key.

        Args:
            key: The key of the node to be deleted.

        Returns:
            The modified tree with the node deleted.
        """

        # If the key is smaller, recurse left until we find the node with the same key
        if key < self.key:
            self.left = self.left.delete_node(key)

        # If the key is larger, recurse right until we find the node to delete
        if key > self.key:
            self.right = self.right.delete_node(key)

        # If the node to delete has no children, then return None, i.e. self.left
        # or self.right = None when called as self.left = self.left.delete_node(key)
        if not self.left and not self.right:
            return None

        # If the node to delete only has a left child, link its parent to its right child
        if not self.left:
            return self.right

        # If the node to delete only has a right child, link its parent to its left child
        if not self.right:
            return self.left

        # If the node has two children, replace it with the smallest 
        # value in the right subtree
        successor = self.find_successor()
        self.key = successor.key
        self.value = successor.value
        self.right = self.right.delete_node(successor.key)

        return self

    def find_successor(self):
        """Find the node with the minimum key in the given right subtree.

        Args:
            node: The subtree to search.

        Returns:
            The node with the minimum key.
        """
        successor = self.right

        while successor.left is not None:
            successor = successor.left

        return successor

    def string_to_number(self, key: str) -> int:
        """Convert a string to a number using its ASCII code.

        Args:
            key: The string to convert to a number.

        Returns:
            A converted string.
        """
        i = 0
        for char in key:
            i += ord(char)

        return i

    def tuple_to_number(self, key: tuple) -> int:
        """Convert a tuple to an integer based on its contents.

        Args:
            key: The tuple to convert.

        Returns:
            A converted tuple.
        """
        i = 0

        # Hash each item individually based on its type and add the hashed values
        for item in key:
            if isinstance(item, (float, int)):
                i += item

            elif isinstance(item, str):
                for char in item:
                    i += ord(char)

            else:
                raise TypeError("The elements in the tuple must be hashable objects")

        return i

    def print_tree(self):
        """Return a string representation of the tree.

        Returns:
            A string representation of the tree
        """
        fragments = []

        if self:

            if self.left:
                fragments.append(f"{self.left.key}: {self.left.value}")
                self.left.print_tree()

            fragments.append(f"{self.key}: {self.value}")

            if self.right:
                fragments.append(f"{self.right.key}: {self.right.value}")
                self.right.print_tree()

        return "{" + ", ".join(fragments) + "}"
