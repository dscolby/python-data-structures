"""This module contains functions to test the HashMap data structure.
"""
import pytest
from python_data_structures.hashmap import HashMap


def test_set_get_items():
    """Test adding to and retrieving items from the hashmap.
    """
    hm = HashMap()
    hm[1] = 'a'
    hm[1.5] = 'b'
    hm['one'] = 'c'
    hm[(1, '2')] = 'd'

    assert hm[1] == 'a'
    assert hm[1.5] == 'b'
    assert hm['one'] == 'c'
    assert hm[(1, '2')] == 'd'


def test_set_wrong_type():
    """Tests that trying to hash a non-hashable item raises an error.
    """
    hm = HashMap()
    msg = "Keys must be either ints, floats, strings, or tuples with those types"
    with pytest.raises(TypeError) as info:
        hm[[1, 2, 3]]

    assert str(info.value) == msg


def test_deletion():
    """Tests deleting items from the hashmap in a Pythonic way.
    """
    hm = HashMap(size=4)

    for i in range(20):
        hm[i] = i + 1

    del hm[1]
    del hm[5]
    del hm[10]
    del hm[15]
    del hm[19]

    assert hm[1] is None
    assert hm[5] is None
    assert hm[10] is None
    assert hm[15] is None
    assert hm[19] is None


def test_rehash():
    """Tests the rehashing functionality.
    """
    hm = HashMap(size=4)

    for i in range(20):
        hm[i] = i + 1

    assert hm[1] == 2
    assert hm[10] == 11


def test_length():
    """Tests the __len__ method works correctly.
    """
    hm = HashMap()
    assert len(hm) == 0

    hm[1] = 1
    assert len(hm) == 1

    hm[1] = "one"
    assert len(hm) == 1

    del hm[1]
    assert len(hm) == 0


def test_getting_items():
    """Test the ability to get a list of key, value tuples.
    """
    hm = HashMap()

    for i in range(5):
        hm[i] = i

    pairs = hm.items()

    assert sum(tpl[0] for tpl in pairs) == 10
    assert sum(tpl[1] for tpl in pairs) == 10


def test_repr():
    """Test printing a hashmap.
    """
    hm = HashMap()
    assert repr(hm) == "()"

    hm['one'] = 1
    assert repr(hm) == "(one => 1)"

    hm['two'] = 2
    assert repr(hm) == "(one => 1, two => 2)"
