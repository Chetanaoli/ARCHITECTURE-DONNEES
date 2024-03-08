from activity2.activity6 import find_tuple_with_most_elements

def test_tuple_with_most_elements_empty_list():
    list_of_tuples = []
    result = find_tuple_with_most_elements(list_of_tuples)
    assert result is None

def test_tuple_with_most_elements_single_empty_tuple():
    list_of_tuples = [()]
    result = find_tuple_with_most_elements(list_of_tuples)
    assert result == None

def test_tuple_with_most_elements_single_tuple():
    list_of_tuples = [(1, 2, 3)]
    result = find_tuple_with_most_elements(list_of_tuples)
    assert result == (1, 2, 3)

def test_tuple_with_most_elements_equal_length_tuples():
    list_of_tuples = [(1, 2), ('a', 'b'), (True, False)]
    result = find_tuple_with_most_elements(list_of_tuples)
    assert result == (1, 2)

def test_tuple_with_most_elements_mixed_data_types():
    list_of_tuples = [(1, 'two', 3), ('a', 'b', 'c', 'd'), (True, False)]
    result = find_tuple_with_most_elements(list_of_tuples)
    assert result == ('a', 'b', 'c', 'd')
