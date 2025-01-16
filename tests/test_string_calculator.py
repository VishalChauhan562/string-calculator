import pytest
from calculator.string_calculator import add

def test_empty_string_returns_zero(): 
    assert add("") == 0


def test_single_number_returns_that_number():
    assert add("1") == 1


def test_two_numbers_returns_their_sum():
    assert add("1,2") == 3


def test_multiple_numbers_returns_their_sum():
    assert add("1,2,3,4,5") == 15    


def test_newlines_between_numbers():
    assert add("1\n2,3") == 6


def test_support_different_delimiter():
    assert add("//;\n1;2") == 3


def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError) as exc:
        add("1,-2,3,-4")
    assert str(exc.value) == "negatives not allowed: -2, -4"