import pytest

from adder_py.adder import add, greet

def test_can_add():
    assert add(1, 2) == 3

def test_can_greet():
    assert greet() == "Hello, Wasmer 🐍!"