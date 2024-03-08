from activity2.activity2 import get_first_word, get_third_from_end, get_programming_language_phrase, reverse_text

def test_extract_word_python():
    text = "Python is a powerful and easy-to-learn programming language."
    result = get_first_word(text)
    assert result == "Python"

def test_extract_word_learn():
    text = "Python is a powerful and easy-to-learn programming language."
    result = get_third_from_end(text)
    assert result == "easy-to-learn"

def test_reverse_string():
    text = "Python is a powerful and easy-to-learn programming language."
    result = reverse_text(text)
    assert result == ".egaugnal gnimmargorp nrael-ot-ysae dna lufrewop a si nohtyP"

