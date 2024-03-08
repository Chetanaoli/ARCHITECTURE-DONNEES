from activity2.activity9 import print_triangle_pattern

def test_display_pyramid_height_1():
    result = print_triangle_pattern(1)
    assert result == None

def test_display_pyramid_height_0():
    result = print_triangle_pattern(0)
    expected_output = None
    assert result == expected_output
