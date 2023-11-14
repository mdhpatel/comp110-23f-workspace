"""Practice with coding and using dictionaries in different problems and situations."""

__author__ = "730710742"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values for every item in a dictionary."""
    new_dict: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] in new_dict:
            raise KeyError("This key already exists in this dictionary.")
        new_dict[dictionary[key]] = key 
    return new_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """This code finds the most frequent color found in a dtionary of colors."""
    color_count: dict[str, int] = dict()
    freq_count: int = 0
    freq_color: str = ""
    for color in dictionary:
        if dictionary[color] in color_count:
            color_count[dictionary[color]] += 1
        else:
            color_count[dictionary[color]] = 1
    for color in color_count:
        if color_count[color] > freq_count:
            freq_count = color_count[color]
            freq_color = color
    return freq_color


def count(word_list: list[str]) -> dict[str, int]:
    """This code will take a list of strings and return a dictionary with corresponding values showing how many times the word appeared in the origional list."""
    count_dict: dict[str, int] = dict()
    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Allows a dictionary to be organized into groups of words depending on first letter that they start with."""
    categorized_words: dict[str, list[str]] = dict()
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in categorized_words:
            categorized_words[first_letter].append(word)
        else:
            categorized_words[first_letter] = [word]
    return categorized_words


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Takes a dictionary of student attendance and allows it to be modified based on new days and new students attending class."""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict