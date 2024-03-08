from activity2.activity3 import add_two_numbers
import builtins
from unittest.mock import patch

def test_addition_valid_input():
    with patch.object(builtins, 'input', side_effect=['5', '7']):
        result = add_two_numbers()
    assert result == 12

def test_addition_negative_input():
    with patch.object(builtins, 'input', side_effect=['-5', '7']):
        result = add_two_numbers()
    assert result == 2
