from activity2.activity10 import get_maximum_number

def test_find_largest_number_positive_numbers():
    result = get_maximum_number(10, 20, 15)
    assert result == 20

def test_find_largest_number_negative_numbers():
    result = get_maximum_number(-5, -8, -3)
    assert result == -3

def test_find_largest_number_mixed_numbers():
    result = get_maximum_number(-10, 5, 0)
    assert result == 5

def test_find_largest_number_equal_numbers():
    result = get_maximum_number(7, 7, 7)
    assert result == 7
