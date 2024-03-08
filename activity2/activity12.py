def check_if_palindrome(word):
    """Checks if a word is a palindrome."""
    return word == word[::-1]

def count_and_list_palindromes(words):
    """Counts and lists palindromes in a given list of words."""
    palindrome_count = 0
    palindrome_list = []

    for w in words:
        if check_if_palindrome(w):
            palindrome_count += 1
            palindrome_list.append(w)

    return palindrome_count, palindrome_list

