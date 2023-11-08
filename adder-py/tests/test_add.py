import pytest

from adder_py.adder import add, greet,json_example

def test_can_add():
    assert add(1, 2) == 3

def test_can_greet():
    assert greet() == "Hello, Wasmer 🐍!"


def test_can_json_roundtrip():
    assert (json_example() ==
            '{"name":"Rob","value":25,"favourite_food":"Beans"}')
