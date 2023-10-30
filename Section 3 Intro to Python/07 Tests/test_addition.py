import addition
import pytest

def test_add():
    assert addition.add(4, 5) == 9

def test_sub(a, b):
    assert addition.sub(4, 5) == -1