"""
This file contains functions to test the functionality of the BinarySearchTree class.
"""
import pytest
from python_data_structures.binary_search_tree import BinarySearchTree


def test_add_and_retrieve():
    """Test adding keys and values to and retrieving them from a treemap.
    """
    treemap = BinarySearchTree()
    treemap.put(1, 1)
    treemap.put("two", 2)
    treemap.put((0, 3, "two"), 5)

    assert treemap.key == 1
    assert treemap.right.key == 346
    assert treemap.right.right.key == 349
    assert treemap.find(1) == 1
    assert treemap.find("two") == 2
    assert treemap.find((0, 3, "two")) == 5
    assert treemap.find(9) is None


def test_add_and_retrieve_non_hashable():
    """Test that we get a key error when trying to add or get non-hashable keys
    """
    treemap = BinarySearchTree()

    with pytest.raises(KeyError) as info:
        treemap.put([1, 2], 2)

    assert str(info.value) == "'Keys must be hashable'"

    with pytest.raises(KeyError) as info:
        treemap.find([1, 2])

    assert str(info.value) == "'Keys must be hashable'"


def test_delete_key():
    """Test adding keys and values to and retrieving them from a treemap.
    """
    treemap = BinarySearchTree()
    treemap.put(1, 1)

    null_tree = treemap.delete_node(1)
    assert null_tree is None

    treemap.put(1, 1)
    treemap.put("two", 2)
    treemap.delete("two")
    assert treemap.find("two") is None
    assert treemap.find("two") is None

    treemap.put(1, 1)
    treemap.put("two", 2)
    treemap.put((0, 3, "two"), 5)
    treemap.delete((0, 3, "two"))
    assert treemap.find((0, 3, "two")) is None
    assert treemap.find((0, 3, "two")) is None


def test_delete_non_hashable():
    """Test to ensure that trying to delete a non-hashable key raises an error
    """
    treemap = BinarySearchTree()
    treemap.put(1, 1)
    treemap.put(100, 5)
    treemap.put(77, 90)

    with pytest.raises(KeyError) as info:
        treemap.delete([3, 4])

    assert str(info.value) == "'Keys must be hashable'"


def test_print_tree():
    """Ensures that we can get a string representation from traversing the tree in-order
    """
    treemap = BinarySearchTree()
    treemap.put(100, 100)
    treemap.put(50, 50)
    treemap.put(200, 200)

    assert treemap.print_tree() == "{50: 50, 100: 100, 200: 200}"
