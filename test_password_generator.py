import pytest
from unittest.mock import patch
import string
from main import get_password_amount, get_password_length, get_user_input, get_user_preferences, password_generator

# Fixture to set up global variables
@pytest.fixture
def setup():
    global uppercase_letters, lowercase_letters, digits, special_characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

# Tests for user input
def test_user_input_no():
    with patch("builtins.input", return_value="no"):
        assert not get_user_input("Do you want to include UPPERCASE letters?")
    
def test_user_input_yes():
    global lower
    with patch("builtins.input", return_value="yes"):
        lower = get_user_input("Do you want to include LOWERCASE letters?")
        assert lower

def test_user_input_invalid_then_valid():
    with patch("builtins.input", side_effect=["wow", "yes"]):
        result = get_user_input("Do you want to include NUMBERS?")
        assert result

def test_user_input_multiple_invalid_then_valid():
    with patch("builtins.input", side_effect=["wow", "crazy", "no"]):
        result = get_user_input("Do you want to include SPECIAL CHARACTERS?")
        assert not result

# Tests for user preferences
def test_user_preferences_all_yes(setup):
    with patch("builtins.input", side_effect=["yes", "yes", "yes", "yes"]):
        preferences = get_user_preferences()
        assert preferences["upper"]
        assert preferences["lower"]
        assert preferences["numbers"]
        assert preferences["s_char"]
        assert uppercase_letters in preferences["all"]
        assert lowercase_letters in preferences["all"]
        assert digits in preferences["all"]
        assert special_characters in preferences["all"]

def test_user_preferences_some_yes(setup):
    with patch("builtins.input", side_effect=["no", "yes", "no", "yes"]):
        preferences = get_user_preferences()
        assert not preferences["upper"]
        assert preferences["lower"]
        assert not preferences["numbers"]
        assert preferences["s_char"]
        assert uppercase_letters not in preferences["all"]
        assert lowercase_letters in preferences["all"]
        assert digits not in preferences["all"]
        assert special_characters in preferences["all"]

def test_user_preferences_none_then_yes(setup):
    with patch("builtins.input", side_effect=["no", "no", "no", "no", "yes", "no", "no", "no"]):
        preferences = get_user_preferences()
        assert preferences["upper"]
        assert not preferences["lower"]
        assert not preferences["numbers"]
        assert not preferences["s_char"]
        assert uppercase_letters in preferences["all"]
        assert lowercase_letters not in preferences["all"]
        assert digits not in preferences["all"]
        assert special_characters not in preferences["all"]

# Tests for password length
def test_get_password_length_eight():
    with patch("builtins.input", return_value="8"):
        assert get_password_length() == 8

def test_get_password_length_seven():
    with patch("builtins.input", side_effect=["7", "continue"]):
        assert get_password_length() == 7

def test_get_password_length_seven_nine():
    with patch("builtins.input", side_effect=["7", "new length", "9"]):
        assert get_password_length() == 9

def test_get_password_length_negative():
    with patch("builtins.input", side_effect=["-1", "8"]):
        assert get_password_length() == 8

## returns number of passwords amount
def test_get_password_amount():
    with patch("builtins.input", return_value = "8"):
        assert get_password_amount() == 8

if __name__ == '__main__':
    pytest.main()
