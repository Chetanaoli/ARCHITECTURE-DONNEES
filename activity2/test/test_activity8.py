from activity2.activity8 import play_guessing_game
from unittest.mock import patch

def test_guess_the_number_incorrect_guess():
    with patch('builtins.input', side_effect=['50', '75', '88', '92', '95']):
        result = play_guessing_game()
    assert result is False

def test_guess_the_number_out_of_attempts():
    with patch('builtins.input', side_effect=['10', '20', '30', '40', '50']):
        result = play_guessing_game()
    assert result is False
