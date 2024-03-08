from activity2.activity1 import count_upper_and_lower

def test_mixed_case_count():
    result = count_upper_and_lower("HelloWorld")
    assert result == (2, 8)

def test_all_lowercase_count():
    result = count_upper_and_lower("hello")
    assert result == (0, 5)

def test_empty_string_count():
    result = count_upper_and_lower("")
    assert result == (0, 0)
