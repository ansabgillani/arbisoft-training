"""
    General group of functions that take a
    random dictionary and random string
    appends a random string to each key in dictionary.
    Demonstrating comprehension, dict.items() and dict.key() loops.
"""


def append_random_string_comprehension(dictionary, random_string) -> dict:
    """
    Appends a random string in dictionary
    using comprehension
    :param random_string: string to be appended
    :param dictionary: dictionary object
    :return: dictionary with appended string
    """
    random_dict = {k: v + random_string for k, v in dictionary.items()}
    return random_dict


def append_random_string_items(dictionary, random_string) -> dict:
    """
    Appends a random string in dictionary
    using d.items()
    :param dictionary: dictionary object
    :param random_string: a random string
    :return: dictionary with appended string
    """
    random_dict = dict()
    for k, v in dictionary.items():
        random_dict[k] = v + random_string

    return random_dict


def append_random_string_keys(dictionary, random_string) -> dict:
    """
    Appends a random string in dictionary
    using keys
    :param dictionary: dictionary object
    :param random_string: a random string
    :return: dictionary with appended string
    """
    random_dict = dict()
    for k in dictionary.keys():
        random_dict[k] = dictionary[k] + random_string

    return random_dict
