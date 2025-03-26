"""This is EX03: The Dictionary Functions Exercise! This file is used for functions."""

__author__: str = "730576361"


def invert(dictionary_1: dict[str, str]) -> dict[str, str]:
    """This function will switch the keys and values in a new dictionary"""
    inverted_dictionary: dict[str, str] = {}
    for key in dictionary_1:
        value = dictionary_1[key]
        inverted_dictionary[value] = key
        if value in inverted_dictionary:
            raise KeyError
        inverted_dictionary[value] = key
    return inverted_dictionary


def count(list_of_something: list[str]) -> dict[str, int]:
    """This function will tally up how many times an item is repeated in a list"""
    final_count: dict[str, int] = {}
    for key in list_of_something:
        if key in final_count:
            final_count[key] += 1
        else:
            final_count[key] = 1
    return final_count


def favorite_color(color_dictionary: dict[str, str]) -> str:
    """This function will find the most popular color based on a dictionary"""
    a: int = 0
    most_popular_color = str()
    counts_of_colors: dict[str, int] = {}
    for key in color_dictionary:
        value = color_dictionary[key]
        if value in counts_of_colors:
            counts_of_colors[value] += 1
        else:
            counts_of_colors[value] = 1
    for value in counts_of_colors:
        if counts_of_colors[value] > a:
            a = counts_of_colors[value]
            most_popular_color = value
    return most_popular_color
