from activity2.activity4 import find_unique_elements

def test_unique_elements_empty_list():
    input_list = []
    result = find_unique_elements(input_list)
    assert result == []

def test_unique_elements_all_unique():
    input_list = [1, 2, 3, 4, 5]
    result = find_unique_elements(input_list)
    assert result == [1, 2, 3, 4, 5]

def test_unique_elements_some_duplicates():
    input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
    result = find_unique_elements(input_list)
    assert result == [1, 2, 3, 4, 5, 6]

def test_unique_elements_mixed_types():
    input_list = [1, '2', '2', 3, 4, 4, '5', 6, 6]
    result = find_unique_elements(input_list)
    assert result == [1, '2', 3, 4, '5', 6]

def test_unique_elements_empty_string():
    input_list = ['']
    result = find_unique_elements(input_list)
    assert result == ['']

def test_unique_elements_nested_lists():
    input_list = [[1, 2], [2, 3], [4, 5], [4, 5]]
    result = find_unique_elements(input_list)
    assert result == [[1, 2], [2, 3], [4, 5]]

def test_unique_elements_mixed_data_types():
    input_list = [1, 2, '2', 3, 4, '4', 5, 6, '6']
    result = find_unique_elements(input_list)
    assert result == [1, 2, '2', 3, 4, '4', 5, 6, '6']
