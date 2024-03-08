def is_word_palindrome(word):
    return word == word[::-1]

def count_palindromic_words(word_list):
    palindrome_count = 0

    for word in word_list:
        if is_word_palindrome(word):
            palindrome_count += 1

    return palindrome_count
