import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from calculator import add, subtract, multiply, combined, divide


# Addition tests

def test_add_positive():
    assert add(3, 4) == 7

def test_add_zeros():
    assert add(0, 0) == 0

def test_add_one_zero():
    assert add(0, 5) == 5

def test_add_negatives():
    assert add(-3, -7) == -10

def test_add_mixed_sign():
    assert add(-3, 7) == 4

def test_add_floats():
    assert add(1.5, 2.5) == pytest.approx(4.0)

def test_add_large_numbers():
    assert add(10**9, 10**9) == 2 * 10**9


# Subtraction tests
def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_zeros():
    assert subtract(0, 0) == 0

def test_subtract_result_negative():
    assert subtract(3, 10) == -7

def test_subtract_negatives():
    assert subtract(-5, -3) == -2

def test_subtract_floats():
    assert subtract(5.5, 2.5) == pytest.approx(3.0)

def test_subtract_same_value():
    assert subtract(7, 7) == 0


# Multiplication tests
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(0, 100) == 0

def test_multiply_both_zeros():
    assert multiply(0, 0) == 0

def test_multiply_negatives():
    assert multiply(-3, -4) == 12

def test_multiply_mixed_sign():
    assert multiply(-3, 4) == -12

def test_multiply_floats():
    assert multiply(2.5, 4.0) == pytest.approx(10.0)

def test_multiply_by_one():
    assert multiply(99, 1) == 99


# Combined tests for add, subtract, and multiply
def test_combined_positive():
    # add(2,3)=5, subtract(2,3)=-1, multiply(2,3)=6 → sum=10
    assert combined(2, 3) == 10

def test_combined_zeros():
    assert combined(0, 0) == 0

def test_combined_negatives():
    # add(-2,-3)=-5, subtract(-2,-3)=1, multiply(-2,-3)=6 → sum=2
    assert combined(-2, -3) == 2

def test_combined_floats():
    # add(1.0,2.0)=3.0, subtract(1.0,2.0)=-1.0, multiply(1.0,2.0)=2.0 → sum=4.0
    assert combined(1.0, 2.0) == pytest.approx(4.0)

# Division tests
def test_divide_positive():
    assert divide(10, 2) == pytest.approx(5.0)

def test_divide_floats():
    assert divide(7.5, 2.5) == pytest.approx(3.0)

def test_divide_negative_numerator():
    assert divide(-10, 2) == pytest.approx(-5.0)

def test_divide_negative_denominator():
    assert divide(10, -2) == pytest.approx(-5.0)

def test_divide_both_negatives():
    assert divide(-10, -2) == pytest.approx(5.0)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_divide_zero_numerator():
    assert divide(0, 5) == pytest.approx(0.0)