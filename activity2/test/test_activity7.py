from activity2.activity7 import reverse_tuples_order

def test_empty_list_reversal():
    list_of_tuples = []
    result = reverse_tuples_order(list_of_tuples)
    assert result == []

def test_single_empty_tuple_reversal():
    list_of_tuples = [()]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [()]

def test_single_tuple_reversal():
    list_of_tuples = [(1, 2, 3)]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [(3, 2, 1)]

def test_multiple_tuples_reversal():
    list_of_tuples = [(1, 2), ('a', 'b', 'c'), (True, False, True, False)]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [(2, 1), ('c', 'b', 'a'), (False, True, False, True)]
