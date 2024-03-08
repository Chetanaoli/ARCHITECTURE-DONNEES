from activity2.activity12 import check_if_palindrome

def test_count_palindromes_empty_input():
    result = check_if_palindrome([])
    assert result == True

def test_count_palindromes_no_palindromes():
    result = check_if_palindrome(["hello", "world", "python"])
    assert result == False

def test_count_palindromes_some_palindromes():
    result = check_if_palindrome(["level", "deed", "hello", "radar"])
    assert result == False

def test_count_palindromes_all_palindromes():
    result = check_if_palindrome(["madam", "racecar", "level", "deed"])
    assert result == False
