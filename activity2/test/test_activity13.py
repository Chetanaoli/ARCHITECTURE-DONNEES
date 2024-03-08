from activity2.activity13 import is_word_palindrome, is_word_palindrome

def test_single_word_is_palindrome_true():
    assert is_word_palindrome("radar") is True

def test_single_word_is_palindrome_false():
    assert is_word_palindrome("python") is False

def test_count_palindromes_empty_input():
    result = is_word_palindrome([])
    assert result == True

def test_count_palindromes_no_palindromes():
    result = is_word_palindrome(["hello", "world", "python"])
    assert result == 0

def test_count_palindromes_some_palindromes():
    result = is_word_palindrome(["level", "deed", "hello", "radar"])
    assert result == False

def test_count_palindromes_all_palindromes():
    result = is_word_palindrome(["madam", "racecar", "level", "deed"])
    assert result == False
