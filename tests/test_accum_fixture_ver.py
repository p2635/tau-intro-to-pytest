(accum):"""
This module has basic unit tests for the accum class.
This is a copy of the test_accum.py class, but the
difference is I've applied the use of fixtures.
I've created this to learn the foundations of pytest.
"""

# -----------------------------------------------
# Imports
# -----------------------------------------------

import pytest
from stuff.accum import Accumulator

# -----------------------------------------------
# Fixtures
# -----------------------------------------------

@pytest.fixture
def accum():
    return Accumulator()

# -----------------------------------------------
# Tests
# -----------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_count_read_only(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
