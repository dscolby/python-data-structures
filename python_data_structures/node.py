"""A module with a simple node class for implementing other data structures."""
from typing import Any

class Node:
    """A simple class to store data for items in other data structures.

    Attributes:
        data: The data to be stored
        next: The next node in the list.
    """
    def __init__(self, data: Any) -> None:
        """Inisialize a Node for a linked list.

        Args:
            data: The data to be stored in the list.
        """
        self.data = data
        self.next = None