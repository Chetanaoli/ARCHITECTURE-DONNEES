from activity2.activity17 import find_symmetric_difference

def test_find_symmetric_difference_empty_sets():
    result = find_symmetric_difference(set(), set())
    assert result == set()

def test_find_symmetric_difference_empty_set1():
    set2 = {1, 2, 3}
    result = find_symmetric_difference(set(), set2)
    assert result == {1, 2, 3}

def test_find_symmetric_difference_empty_set2():
    set1 = {1, 2, 3}
    result = find_symmetric_difference(set1, set())
    assert result == {1, 2, 3}

def test_find_symmetric_difference_no_symmetric_difference():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    result = find_symmetric_difference(set1, set2)
    assert result == {1, 2, 3, 4, 5, 6}

def test_find_symmetric_difference_some_symmetric_difference():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = find_symmetric_difference(set1, set2)
    assert result == {1, 2, 5, 6}

def test_find_symmetric_difference_all_symmetric_difference():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = find_symmetric_difference(set1, set2)
    assert result == {1, 2, 5, 6}
