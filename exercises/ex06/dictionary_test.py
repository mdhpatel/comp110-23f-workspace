"""Practicing writng unit tests for each function created in the previous exercise."""

__author__ = "730710742"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_empty_dict() -> None:
    """Invert should return an empty dictionary when given an empty dictionary with no as an argument."""
    assert invert({}) == {}


def test_invert_one_key() -> None:
    """If a dictionary has one key, the invert function should still swap the key and element."""
    assert invert({"Maanav": "Patel"}) == ({"Patel": "Maanav"})


def test_invert_two_keys() -> None:
    """If a dictionary has two keys, the invert function should swap both the keys and the elements for both parts of the dictionary."""
    assert invert({"cat": "dog", "turtle": "bird"}) == ({"dog": "cat", "bird": "turtle"})


def test_favorite_color_empty_dict() -> None:
    """If test favorite color receives an empty dictionary then it should not output or return any string."""
    assert favorite_color({}) == ""


def test_favorite_color() -> None:
    """The function should return a string showing what the most frequent color found in the dictionary was."""
    assert favorite_color({"Maanav": "red", "John": "blue", "Jake": "pink", "Josh": "red"}) == "red"


def test_favorite_color_with_tie() -> None:
    """If there is a tie in the most frequently appearing color in a dictionary then the fucntion should output the color that appears first."""
    assert favorite_color({"Maanav": "red", "John": "blue", "Jake": "pink", "Josh": "red", "Kate": "blue"}) == "red"


def test_count_empty_list() -> None:
    """If the function recives an empty list then the output should be an empty dictionary."""
    assert count([]) == {}


def test_count() -> None:
    """The function should return a dictionary that shows how many times each word in a list appears in that list."""
    assert count(["dog", "cat", "dog", "frog", "pig", "dog", "dog"]) == ({"dog": 4, "cat": 1, "frog": 1, "pig": 1})


def test_count_one_appearance() -> None:
    """The function should still return a dictionary with the number of instances found of each word in the list even if there is only one instance of each word."""
    assert count(["dog", "cat", "chicken", "frog", "pig", "horse"]) == ({"dog": 1, "cat": 1, "chicken": 1, "frog": 1, "pig": 1, "horse": 1})


def test_alphabetizer_empty_list() -> None:
    """The function should return an empty dictionary if the arguemtn list is empty as well."""
    assert alphabetizer([]) == {}


def test_alphabetizer() -> None:
    """The function should return a dictionary of words from a list that are organized by the first letter they start with."""
    assert alphabetizer(["dogs", "cat", "door", "dart", "frog", "frost", "camp"]) == ({"d": ["dogs", "door", "dart"], "c": ["cat", "camp"], "f": ["frog", "frost"]})


def test_alphabetizer_one_word() -> None:
    """If the function only receives a list of one word as the argument, then the function should still output a dictionary, only that dictionary will have only one key and one element."""
    assert alphabetizer(["snow"]) == ({"s": ["snow"]})


def test_update_attendance_empty_argument() -> None:
    """If the function receives empty dictionary and list arguments but still receives words for its string arguments, the function should output a dictionary made out of the two other arguments."""
    assert update_attendance({}, "Monday", "Maanav") == ({"Monday": ["Maanav"]})


def test_update_attendance() -> None:
    """The function should output a dictionary that shows all students present in the form of a list on a given day."""
    assert update_attendance({"Monday": ["Maanav", "Eve", "Kate", "Jake"], "Tuesday": ["Maanav", "Josh", "Keisha"]}, "Monday", "Jack") == ({"Monday": ["Maanav", "Eve", "Kate", "Jake", "Jack"], "Tuesday": ["Maanav", "Josh", "Keisha"]})


def test_update_attendance_double_value() -> None:
    """The function should add Ethan to the list of students present for class on Monday after looping through the larger list."""
    assert update_attendance({"Monday": ["Maanav", "Jake", "Steven", "Clara", "Jordan", "Eve"], "Tuesday": ["Maanav", "Kate", "Chris"]}, "Monday", "Ethan") == ({"Monday": ["Maanav", "Jake", "Steven", "Clara", "Jordan", "Eve", "Ethan"], "Tuesday": ["Maanav", "Kate", "Chris"]})
