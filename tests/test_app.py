import pytest

MOCK_DICTIONARY = {
    "first_name": "Jorge",
    "last_name": "Guzman",
    "active": 1,
    "age": 99,
}

def test_dictionary_has_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)


