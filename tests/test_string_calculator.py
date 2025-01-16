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