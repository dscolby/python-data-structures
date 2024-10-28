"""A module with a simple linked list class implemented from scratch.
"""
from typing import Any, Iterable
from python_data_structures.node import Node


class LinkedList:
    """A simple linked list class.
    """

    def __init__(self) -> None:
        """Initialize a new singly linked list.
        """
        self._head = None
        self._len = 0
        self._index = 0
        self._current_node = self._head

    def add_left(self, data: Any) -> None:
        """Add a new item to the beginning of a singly linked list

        Args:
            data: The data to add to the list
        """
        if data is None:
            raise TypeError("The data to add cannot be None")

        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._current_node = self._head

        else:
            new_node.next = self._head
            self._head = new_node
            self._current_node = self._head

        self._len += 1

    def add_right(self, data: Any) -> None:
        """Add a new item to the end of a linked list.

        Args:
            data: The data to add to the list.
        """
        if data is None:
            raise TypeError("The data to add cannot be None")

        current_node = self._head
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._current_node = self._head
            return

        else:
            while current_node.next:
                current_node = current_node.next

        current_node.next = new_node

    def __len__(self):
        return self._len

    def __repr__(self):
        first_parenthesis, last_parenthesis = "[", "]"
        current_node = self._head

        if current_node is None:
            return first_parenthesis + last_parenthesis

        while current_node is not None:
            first_parenthesis = first_parenthesis + str(current_node.data)

            if current_node.next is not None:
                first_parenthesis = first_parenthesis + ", "

            current_node = current_node.next

        return first_parenthesis + last_parenthesis

    def __getitem__(self, key: int) -> Any:
        if key < -1:
            raise IndexError("The index is not in the range of the list")

        if key > self._len:
            raise IndexError(
                f"The index is out of range of the list, whose length is {self._len}"
            )

        if key == -1:
            key += self._len

        idx = 0
        current_node = self._head

        # Keep going to the next item until we get to the correct index
        while idx < key:
            current_node = current_node.next
            idx += 1

        return current_node.data

    def __setitem__(self, key: int, value: Any) -> None:
        if key < -1:
            raise IndexError("The index must be within the range of the list or -1")

        if key > self._len:
            raise IndexError(
                f"The index is out of the range of the list, whose length is {self._len}"
            )

        # No need to reinvent the wheel
        if key == 0:
            self.add_left(value)
            return

        # Same thing and also using -1 indexing for Pythonic behavior
        if key == self._len or key == -1:
            self.add_right(value)
            return

        new_node = Node(value)
        idx = 0
        current_node = self._head

        # Iterate until the index before where we want to add the new data
        while idx < key - 1:
            idx += 1
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def __delitem__(self, key: int) -> None:
        if key == -1:
            key = self._len - 1

        if key < 0 or key >= self._len:
            return

        if key == 0 and self._head.next is not None:
            self._head = self._head.next
            self._len -= 1
            return

        if key == 0 and self._head.next is None:
            self._head = None
            self._len -= 1
            return

        idx = 0
        current_node = self._head

        while idx < key - 1:
            current_node = current_node.next
            idx += 1

        node_to_delete = current_node.next
        current_node.next = node_to_delete.next

        self._len -= 1

    def __add__(self, other: Iterable):
        for i in other:
            self.add_right(i)
            self._len += 1

        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._len:
            raise StopIteration

        else:
            current_node = self._current_node
            self._current_node = self._current_node.next
            self._index += 1
            return current_node.data
