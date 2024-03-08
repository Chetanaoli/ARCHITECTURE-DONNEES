from activity2.activity11 import decode_ascii_message

def test_valid_input_decoding():
    result = decode_ascii_message("72 101 108 108 111")
    assert result == "Hello"

def test_empty_input_decoding():
    result = decode_ascii_message("")
    assert result == ""

def test_invalid_input_decoding():
    result = decode_ascii_message("72 invalid 108 111")
    assert result == 'Invalid Decoding'

def test_negative_numbers_decoding():
    result = decode_ascii_message("72 -101 108 111")
    assert result == "Invalid Decoding"

def test_float_numbers_decoding():
    result = decode_ascii_message("72 101.5 108 111")
    assert result == "Invalid Decoding"
