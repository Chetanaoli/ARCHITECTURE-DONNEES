from activity2.activity5 import rotate_list_right

def test_single_element_rotation():
    input_list = [42]
    rotation = 2
    result = rotate_list_right(input_list, rotation)
    assert result == [42]

def test_rotation_greater_than_length():
    input_list = [1, 2, 3, 4, 5]
    rotation = 7
    result = rotate_list_right(input_list, rotation)
    assert result == [4, 5, 1, 2, 3]

def test_rotation_equal_to_length():
    input_list = [1, 2, 3, 4, 5]
    rotation = 5
    result = rotate_list_right(input_list, rotation)
    assert result == [1, 2, 3, 4, 5]

def test_mixed_data_types_rotation():
    input_list = ['a', 'b', 'c', 'd', 'e']
    rotation = 2
    result = rotate_list_right(input_list, rotation)
    assert result == ['d', 'e', 'a', 'b', 'c']

def test_negative_rotation():
    input_list = [10, 20, 30, 40, 50]
    rotation = -2
    result = rotate_list_right(input_list, rotation)
    assert result == [30, 40, 50, 10, 20]
