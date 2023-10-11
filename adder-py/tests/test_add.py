import pytest

from adder_py.adder import add

def test_can_add():
    assert add(1, 2) == 3

