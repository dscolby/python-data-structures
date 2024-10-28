"""A module with a simple stack data structure implemented from scratch.
"""
from typing import Any
from python_data_structures.node import Node

class Stack:
    """A simple stack implementation that doesn't rely on any built in data structures.
    """
    def __init__(self) -> None:
        """Initialize a stack.
        """
        self._top = None
        self._size = 0

    def is_empty(self) -> bool:
        """Is the stack empty?

        Returns:
            True if the stack is empty, otherwise False.
        """
        return self._top is None

    def peek(self) -> Any:
        """Get the next item in the stack without deleting it.

        Returns:
            The next item in the stack.
        """
        return self._top.data if self._top is not None else None

    def push(self, data: Any) -> None:
        """Add an item to the top of the stack.

        Args:
            data: The data to be added to the stack.
        """
        new_node = Node(data)

        if self._top is None:
            self._top = new_node

        else:
            new_node.next = self._top
            self._top = new_node

        self._size += 1

    def pop(self) -> Any:
        """Get the next item in the stack and delete it.

        Returns:
            The next item in the stack.
        """
        if self._top is None:
            return
        else:
            item = self._top.data
            self._top = self._top.next
            self._size -= 1
            return item

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        first_parenthesis, last_parenthesis = "[", "]"
        current_node = self._top

        if self._top is None:
            return first_parenthesis + last_parenthesis

        while current_node is not None:
            first_parenthesis = first_parenthesis + str(current_node.data)

            if current_node.next is not None:
                first_parenthesis = first_parenthesis + ", "

            current_node = current_node.next

        return first_parenthesis + last_parenthesis
