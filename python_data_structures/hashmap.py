"""This module contains a simple hashmap implementation.
"""
from typing import Union, Any
import math

class HashMap:
    """A simple implementation of a hashmap with multiplicative hashing.

    Attributes:
        A: Knuth's recommended constant for multiplicative hashing.
    """
    A = (math.sqrt(5) - 1) / 2  # The constant value recommended by Knuth

    class HashNode:
        """A node class to store keys, values, and implement linear probing.

        Attributes:
            key: The key.
            value: The corresponding value.
            next: The next node.
        """
        def __init__(self, key: Union[int, float, str, tuple], value: Any):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, size : int=256, capacity : float=0.75) -> None:
        """Initialize a hash table.

        Args:
            size: the initial capacity of the hash table.
            capacity: The proportion of slots that are filled before rehashing.
        """
        self._size = size
        self._max_capacity = capacity
        self._table = [None] * size
        self._len = 0
        self._index = 0

    # Just a method to dispatch to the right hash method based on the input type
    def _hash(self, key: Union[int, float, str, tuple]):
        if isinstance(key, (int, float)):
            return self._hash_number(key)

        if isinstance(key, str):
            return self._hash_str(key)

        if isinstance(key, tuple):
            return self._hash_tuple(key)

        raise TypeError(
            "Keys must be either ints, floats, strings, or tuples with those types"
        )

    def _hash_number(self, key: Union[int, float]) -> int:
        return math.floor((self.A * key - math.floor(self.A * key)) * self._size)

    def _hash_str(self, key: str) -> int:
        i = 0
        for char in key:
            i += ord(char)

        return self._hash_number(i)

    def _hash_tuple(self, key: tuple) -> int:
        i = 0

        # Hash each item individually based on its type and add the hashed values
        for item in key:
            if isinstance(item, (float, int)):
                i += item

            elif isinstance(item, str):
                i += ord(item)

            else:
                raise TypeError("The elements in the tuple must be hashable objects")

        return self._hash_number(i)

    def _insert(self, key: Union[int, float, str, tuple], value: Any) -> None:
        idx = self._hash(key)
        new_node = HashMap.HashNode(key, value)

        # If there's nothing at the index yet, we just add the node there
        if not self._table[idx]:
            self._table[idx] = new_node
            self._len += 1
            return

        current_node = self._table[idx]

        # If the current node has the same key, just update the value
        if current_node.key == key:
            current_node.value = value
            return

        # Walk down the chain until we reach the last node
        while current_node:

            # If we reach a node with the same key, just replace the value
            if current_node.key == key:
                current_node.value = value
                return

            # Add the new node to the end of the chain
            if not current_node.next:
                current_node.next = new_node
                break

            current_node = current_node.next

        self._len += 1

    def _rehash(self):
        self._size *= 2
        old_table = self._table
        self._table = [None] * self._size

        for i in old_table:
            if i:  # If there's an item in the table, walk down the chain
                current_node = i
                while current_node:
                    self._insert(current_node.key, current_node.value)
                    current_node = current_node.next

    def items(self) -> list:
        """Get a list of the keys and values in the hashmap.

        Returns:
            A list of tuples that contain a key and its value.
        """
        results = []

        for node in self._table:
            if node:
                current_node = node

                while current_node:
                    results.append((current_node.key, current_node.value))
                    current_node = current_node.next

        return results

    def __len__(self):
        return self._len

    def __getitem__(self, key: Union[int, float, str, tuple]) -> Any:
        idx = self._hash(key)

        # Return nothing if there is no value at the given key
        if not self._table[idx]:
            return None

        current_node = self._table[idx]

        # Loop through the stack until we get to the last noed 
        # or find a node with the right key
        while current_node.next:
            if current_node.key == key:
                return current_node.value

            current_node = current_node.next

        # Return nothing if we don't find a node with the original key at the hashed index
        return current_node.value if current_node.value else None

    def __setitem__(self, key: Union[int, float, str, tuple], value: Any) -> Any:
        if self._len / self._size >= self._max_capacity:
            self._rehash()

        self._insert(key, value)

    def __delitem__(self, key: Union[int, float, str, tuple]):
        for i, node in enumerate(self._table):
            if node:
                current_node = node

                # If there's only a single node and not a linked list
                if (not current_node.next) and (current_node.key == key):
                    self._table[i] = None
                    self._len -= 1
                    return

                while current_node:
                    if not current_node.next:
                        break

                    next_node = current_node.next

                    if next_node.key == key:
                        current_node.next = next_node.next
                        self._len -= 1

    def __repr__(self):
        first_parenthesis, last_parenthesis = "(", ")"

        if all(not i for i in self._table):
            return first_parenthesis + last_parenthesis

        key_value_pairs = []
        for i in self._table:
            if i:
                current_node = i
                while current_node:
                    temp_out = str(current_node.key) + " => " + str(current_node.value)
                    key_value_pairs.append(temp_out)
                    current_node = current_node.next

        return first_parenthesis + ", ".join(key_value_pairs) + last_parenthesis
    