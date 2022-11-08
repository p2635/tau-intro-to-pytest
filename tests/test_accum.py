"""
This module has basic unit tests for the accum class.
I've created this to learn the foundations of pytest.
"""

# -----------------------------------------------
# Imports
# -----------------------------------------------

import pytest
from stuff.accum import Accumulator

# -----------------------------------------------
# Tests
# -----------------------------------------------

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0

def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_count_read_only():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
