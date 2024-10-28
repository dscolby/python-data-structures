"""A module with a simple queue data structure implemented from scratch.
"""
from typing import Any
from python_data_structures.node import Node

class Queue:
    """A simple queue class implemented from scratch.
    """

    def __init__(self, size: int) -> None:
        """Initialize a queue.

        Args:
            size: The size of the queue.
        """
        self._first = None
        self._size = size
        self._items = 0

    def is_empty(self) -> bool:
        """Is the queue empty?

        Returns:
            True if the queue is empty, otherwise False.
        """
        return self._items == 0

    def is_full(self) -> bool:
        """Is the queue full?

        Returns:
            True is the queue is full, otherwise False.
        """
        return self._items == self._size

    def peek(self) -> Any:
        """Get the next item in the queue without deleting it.

        Returns:
            The next item in the queue.
        """
        if self._first is None:
            return None

        return self._first.data

    def enque(self, data: Any) -> None:
        """Add an item to the queue.

        Args:
            data: The data to be added to the queue.
        """
        if self.is_full():
            raise IndexError("The queue is already full")

        new_node = Node(data)

        if self._first is None:
            self._first = new_node

        else:
            current_node = self._first
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

        self._items += 1

    def dequeue(self) -> Any:
        """Remove the next item from teh queue.

        Returns:
            The next item in the queue.
        """
        if self._first is None:
            return None

        return_data = self._first.data

        if self._first.next is not None:
            self._first = self._first.next

        else:
            self._first = None

        self._items -= 1
        return return_data

    def __len__(self):
        return self._items

    def __repr__(self):
        first_parenthesis, last_parenthesis = "[", "]"
        current_node = self._first

        if self._first is None:
            return first_parenthesis + last_parenthesis

        while current_node is not None:
            first_parenthesis = first_parenthesis + str(current_node.data)

            if current_node.next is not None:
                first_parenthesis = first_parenthesis + ", "

            current_node = current_node.next

        return first_parenthesis + last_parenthesis
