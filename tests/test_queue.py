"""Test to ensure the correctness of the queue data structure.
"""
import pytest
from python_data_structures.queue import Queue


def test_is_empty():
    """Test the is_empty method.
    """
    q = Queue(5)
    assert q.is_empty()

    q.enque(9)
    assert not q.is_empty()


def test_is_full():
    """Test the is_full method.
    """
    q = Queue(2)
    assert not q.is_full()

    q.enque(6)
    q.enque(4)
    assert q.is_full()

    q.dequeue()
    assert not q.is_full()


def test_peek():
    """Test that the peek method works correctly.
    """
    q = Queue(3)
    assert q.peek() is None

    q.enque(6)
    assert q.peek() == 6
    assert q._first.data == 6

    q.dequeue()
    assert q.is_empty()


def test_enqueue():
    """Test adding items to the queue.
    """
    q = Queue(2)
    q.enque(1)
    q.enque(2)
    assert q._first.data == 1
    assert q._items == 2


def test_enqueue_full_error():
    """Test adding items to a full queue raises an error.
    """
    q = Queue(2)
    q.enque(1)
    q.enque(2)

    with pytest.raises(IndexError) as info:
        q.enque(4)

    assert str(info.value) == "The queue is already full"

def test_dequeue():
    """Test removing items from a queue.
    """
    q = Queue(2)
    assert q.dequeue() is None

    q.enque(1)
    assert q.dequeue() == 1
    assert q._first is None


def test_length():
    """Test that the __len__ method works.
    """
    q = Queue(2)
    assert len(q) == 0

    q.enque(1)
    assert len(q) == 1

    q.dequeue()
    assert len(q) == 0


def test_repr():
    """Test that the __repr__ method works.
    """
    q = Queue(2)
    assert repr(q) == "[]"

    q.enque(1)
    assert repr(q) == "[1]"

    q.enque(2)
    assert repr(q) == "[1, 2]"
