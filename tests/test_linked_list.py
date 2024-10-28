"""Functions to test the correctness of the linked list implementation.
"""
import pytest
from python_data_structures.linked_list import LinkedList


def test_add_left():
    """Test adding items to the beginning of a linked list works correctly.
    """
    lst = LinkedList()
    lst.add_left(6)
    lst.add_left("six")
    lst.add_left([])
    node_1 = lst._head
    node_2 = node_1.next
    node_3 = node_2.next

    assert node_1.data == []
    assert node_2.data == "six"
    assert node_3.data is 6
    assert node_3.next is None


def test_add_left_none():
    """Test that adding a value of None to the beginning of a linked list raises an error.
    """
    lst = LinkedList()
    with pytest.raises(TypeError) as info:
        lst.add_left(None)

    assert str(info.value) == "The data to add cannot be None"


def test_add_right():
    """Test adding items to the end of a linked list works correctly.
    """
    lst = LinkedList()
    lst.add_right(6)
    lst.add_right("six")
    lst.add_right([])
    node_1 = lst._head
    node_2 = node_1.next
    node_3 = node_2.next

    assert node_1.data == 6
    assert node_2.data == "six"
    assert node_3.data == []
    assert node_3.next is None


def test_add_right_none():
    """Test that adding a value of None to the end of a linked list raises an error.
    """
    lst = LinkedList()
    with pytest.raises(TypeError) as info:
        lst.add_right(None)

    assert str(info.value) == "The data to add cannot be None"


def test_length():
    """Test the correctness of the __len__ method.
    """
    lst = LinkedList()
    assert len(lst) == 0

    for i in range(3):
        lst.add_left(i)

    assert len(lst) == 3

    del lst[2]
    assert len(lst) == 2

    result = lst + [1, 2]
    assert len(result) == 4


def test_repr():
    """Test the output of the __repr__ method.
    """
    lst = LinkedList()
    output = repr(lst)
    assert output == "[]"

    lst.add_right([])
    output = repr(lst)
    assert output == "[[]]"

    lst.add_right(9)
    output = repr(lst)
    assert output == "[[], 9]"


def test_get_item():
    """Test getting items from an index.
    """
    lst = LinkedList()
    lst = lst + [1, 2, 3, 4, 5]

    assert lst[-1] == 5
    assert lst[0] == 1
    assert lst[3] == 4


def test_get_item_error():
    """Test that we can only get items from valid indices.
    """
    lst = LinkedList()
    lst = lst + [1, 2, 3]

    with pytest.raises(IndexError) as info:
        lst[10]

    assert str(info.value) == "The index is out of range of the list, whose length is 3"

    with pytest.raises(IndexError) as info:
        lst[-2]

    assert str(info.value) == "The index is not in the range of the list"


def test_set_item():
    """Test setting items at a valid index.
    """
    lst = LinkedList()
    lst = lst + [1, 2, 3]

    lst[0] = 0
    assert lst[0] == 0 and lst[1] == 1

    lst[4] = 4
    assert lst[4] == 4 and lst[3] == 3

    lst[2] = 7
    assert lst[2] == 7 and lst[3] == 2


def test_set_item_error():
    """Test that setting items at an invalid index raises an error.
    """
    lst = LinkedList()
    lst = lst + [1, 2, 3]

    with pytest.raises(IndexError) as info:
        lst[10] = 3

    assert str(info.value) == "The index is out of the range of the list, whose length is 3"

    with pytest.raises(IndexError) as info:
        lst[-2] = 2

    assert str(info.value) == "The index must be within the range of the list or -1"


def test_deletion():
    """Test that we can delete items at a valid index.
    """
    lst = LinkedList()
    lst = lst + [1, 2]

    del lst[-1]
    assert lst._head.next is None

    del lst[-5]
    assert lst._head.data == 1

    del lst[10]
    assert lst._head.data == 1

    del lst[0]
    assert lst._head is None

    lst = LinkedList()
    lst = lst + [1, 2, 3, 4, 5, 6]
    del lst[0]
    assert lst[0] == 2

    del lst[2]
    assert lst[2] == 5

    del lst[3]
    assert lst[-1] == 5


def test_add():
    """Test the ability to add a linked list with an iterable.
    """
    lst = LinkedList()
    lst = lst + [1, 2, 3]
    assert len(lst) == 3

    lst = lst + (4, 5)
    assert len(lst) == 5


def test_iteration():
    """Test that we can iterate through a linked list.
    """
    lst = LinkedList()
    lst = lst + [1, 2, 3]

    assert [i for i in lst] == [1, 2, 3]
