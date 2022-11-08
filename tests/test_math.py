"""
This module has basic unit tests for math operations.
I've created this to learn the foundations of pytest.
"""

# -----------------------------------------------
# Imports
# -----------------------------------------------

import pytest

# -----------------------------------------------
# Chapter 1 - Positive test case
# -----------------------------------------------
@pytest.mark.fave
def test_one_plus_one():
    assert 1 + 1 == 2

# -----------------------------------------------
# Chapter 2 - Negative test case - this should fail
# and show assertion introspection.
# -----------------------------------------------
def test_one_plus_two():
    a = 1
    b = 2
    c = 10
    assert (a + b) == c

# -----------------------------------------------
# Chapter 3 - A test function that verifies
# an exception.
# -----------------------------------------------
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

# -----------------------------------------------
# Chapter 4 - Learning the DRY principle with
# parametrized test functions.
# -----------------------------------------------
products = [
    (5, 5, 25),              # Positive ints
    (1, 55, 55),             # Identity
    (0, 55, 0),              # Zero
    (5, -5, -25),            # Positive by negative
    (-5, -5, 25),            # Negative by negative
    (2.5, 5.5, 13.75),       # Floats
]
@pytest.mark.parametrize('a, b, product', products)
def test_multiply(a, b, product):
    assert a * b == product
