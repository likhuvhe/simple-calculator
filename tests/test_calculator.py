import pytest
from simple_calculator.calculator import add, multiply

def test_add():
    assert add(1, 2) == 3
def test_1_add():
    assert add(-1, -1) == -2
def test_2_add():
    assert add(1,2,3,4,5) == 15

def test_multiply():
    assert multiply(1,3) == 3
def test_1_multiply():
    assert multiply(-1,3) == -3
def test_2_multiply():
    assert multiply(1,2,3,4,5) == 120