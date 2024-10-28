"""Test the functionality of the stack implementation.
"""
from python_data_structures.stack import Stack


def test_is_empty():
    """Test that the is_empty method works.
    """
    stack = Stack()

    assert stack.is_empty()

    stack.push(5)
    assert stack.is_empty() is False

    stack.pop()
    assert stack.is_empty()


def test_peek():
    """Test that the peek method works properly.
    """
    stack = Stack()
    assert stack.peek() is None

    stack.push(5)
    assert stack.peek() == 5

    stack.push(6)
    assert stack.peek() == 6


def test_push():
    """Test pushing items to the stack.
    """
    stack = Stack()
    stack.push(5)

    assert stack._top.data == 5

    stack.push(9)
    assert stack._top.next.data == 5


def test_pop():
    """Test popping items from the stack.
    """
    stack = Stack()
    assert stack.pop() is None

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack._top.data == 2
    assert stack._top.next.data == 1


def test_length():
    """Test the __len__ method.
    """
    stack = Stack()
    assert len(stack) == 0

    stack.push(8)
    assert len(stack) == 1


def test_repr():
    """Test the __repr__ method.
    """
    stack = Stack()
    assert repr(stack) == "[]"

    stack.push(6)
    assert repr(stack) == "[6]"

    stack.push(99)
    assert repr(stack) == "[99, 6]"
