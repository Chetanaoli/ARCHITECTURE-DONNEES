def get_first_word(input_text):
    return input_text.split()[0]

def get_third_from_end(input_text):
    return input_text.split()[-3]

def get_programming_language_phrase(input_text):
    start_index = input_text.find("powerful")
    end_index = input_text.find("language") + len("language")
    return input_text[start_index:end_index]

def reverse_text(input_text):
    return input_text[::-1]
