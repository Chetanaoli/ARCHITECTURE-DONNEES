from activity2.activity19 import iterate_and_increment_bytearray

def test_iterate_and_increment_empty_bytearray(capsys):
    byte_array = bytearray()
    iterate_and_increment_bytearray(byte_array)

    captured = capsys.readouterr()
    assert captured.out == ""

def test_iterate_and_increment_non_empty_bytearray(capsys):
    byte_array = bytearray([65, 66, 67])
    iterate_and_increment_bytearray(byte_array)

    captured = capsys.readouterr()
    assert captured.out == "Element 1: 65\nElement 2: 66\nElement 3: 67\n"

    assert byte_array == bytearray([66, 67, 68])

