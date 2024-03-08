from activity2.activity16 import find_intersection

def test_empty_sets_intersection():
    result = find_intersection(set(), set())
    assert result == set()

def test_empty_set2_intersection():
    set1 = {1, 2, 3}
    result = find_intersection(set1, set())
    assert result == set()

def test_no_intersection():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    result = find_intersection(set1, set2)
    assert result == set()

def test_some_intersection():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = find_intersection(set1, set2)
    assert result == {3, 4}

def test_all_intersection():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = find_intersection(set1, set2)
    assert result == {3, 4}
