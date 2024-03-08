from activity2.activity18 import update_bytearray_element

def test_valid_index_bytearray_modification():
    input_list = [65, 66, 67, 68]
    index = 2
    new_value = 69
    result = update_bytearray_element(input_list, index, new_value)
    assert result == bytearray([65, 66, 69, 68])

def test_invalid_index_bytearray_modification():
    input_list = [65, 66, 67, 68]
    index = 5
    new_value = 69
    result = update_bytearray_element(input_list, index, new_value)
    assert result is None

def test_negative_index_bytearray_modification():
    input_list = [65, 66, 67, 68]
    index = -2
    new_value = 69
    result = update_bytearray_element(input_list, index, new_value)
    assert result is None

def test_empty_list_bytearray_modification():
    input_list = []
    index = 0
    new_value = 69
    result = update_bytearray_element(input_list, index, new_value)
    assert result is None
