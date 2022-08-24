"""
This module contains basic unit test for math operations
Their purpose is to show how to use the pytest framework by example
"""

""" Imports """
import pytest

""" A test case that verifes an exception """


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

        assert 'division by zero' in str(e.value)


""" A test case which results in PASS """


def test_one_plus_one():
    assert 1 + 1 == 2


""" A test case which results in FAIL """


def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


""" A test case which results in Exception """


def test_divide_by_zero():
    num = 1 / 0


# Parmetrized

product = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]


@pytest.mark.parametrize('a,b,product',product)
def test_multilication(a, b, product):
    assert a * b == product
