"""This is also EX03! But this file will be used for unit tests."""

__author__: str = "730576361"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count

import pytest

"""Allows pytest to run in the 1st unit test for KeyError below."""


"""3x Unit Tests for invert Function"""


def test_invert_keyerror() -> None:
    """Tests for an invert function that raises a KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {
            "fruit": "apple",
            "snack": "apple",
        }
        invert(my_dictionary)


def test_invert_foods() -> None:
    """Tests an invert function that uses a dict of foods."""
    dictionary_1: dict[str, str] = {
        "fruit": "apple",
        "vegetable": "carrot",
        "protein": "chicken",
    }
    assert invert(dictionary_1) == {
        "apple": "fruit",
        "carrot": "vegetable",
        "chicken": "protein",
    }


def test_invert_sports() -> None:
    """Test an invert function that uses a dict filled with sports."""
    dictionary_1: dict[str, str] = {"football": "soccer", "basketball": "tennis"}
    assert invert(dictionary_1) == {"soccer": "football", "tennis": "basketball"}


"""3x Unit Tests for count Function"""


def test_count_empty_list() -> None:
    """Tests a count function containing an empty list."""
    final_count: list[str] = []
    assert count(final_count) == {}


def test_count_sports() -> None:
    """Test a count function using a list of sports."""
    final_count: list[str] = [
        "basketball",
        "basketball",
        "basketball",
        "football",
        "football",
        "soccer",
    ]
    assert count(final_count) == {"basketball": 3, "football": 2, "soccer": 1}


def test_count_animals() -> None:
    """Tests a count function using a list of animals."""
    final_count: list[str] = ["monkey", "monkey", "bear", "llama"]
    assert count(final_count) == {"monkey": 2, "bear": 1, "llama": 1}


"""3x Unit Tests for favorite_color Function"""


def test_favorite_color_empty_dict() -> None:
    """Tests a favorite_color function containing an empty dictionary."""
    color_dictionary: dict[str, str] = {}
    assert favorite_color(color_dictionary) == ""


def test_favorite_color_autumn() -> None:
    """Tests a favorite_color function using a dictionary of autumnal colors."""
    color_dictionary: dict[str, str] = {
        "Hailey": "orange",
        "Lauren": "yellow",
        "Natalie": "yellow",
        "Kayla": "red",
    }
    assert favorite_color(color_dictionary) == "yellow"


def test_favorite_color_duplicate() -> None:
    """Tests a favorite_color function using a tie for favorite color."""
    color_dictionary: dict[str, str] = {
        "Hailey": "purple",
        "Lauren": "purple",
        "Natalie": "blue",
        "Kayla": "blue",
    }
    assert favorite_color(color_dictionary) == "purple"
    """The color that is chosen to win the tie is the one that appeared first."""
