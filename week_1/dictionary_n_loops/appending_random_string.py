def append_random_string_comprehension(d, s) -> dict:
    """
    Appends a random string in dictionary
    using comprehension
    :param d: dictionary object
    :param s: a random string
    :return: dictionary with appended string
    """
    random_dict = {k: v + s for k, v in d.items()}
    return random_dict


def append_random_string_items(d, s) -> dict:
    """
    Appends a random string in dictionary
    using d.items()
    :param d: dictionary object
    :param s: a random string
    :return: dictionary with appended string
    """
    random_dict = dict()
    for k, v in d.items():
        random_dict[k] = v + s

    return random_dict


def append_random_string_keys(d, s) -> dict:
    """
    Appends a random string in dictionary
    using keys
    :param d: dictionary object
    :param s: a random string
    :return: dictionary with appended string
    """
    random_dict = dict()
    for k in d.keys():
        random_dict[k] = d[k] + s

    return random_dict
