"""
Group of functions that search all instances of a key in a list.
Functions do same thing but with different looping mechanism.
"""


def search_key_first(nums: list[int], key: int) -> list[int]:
    """
    Traversal with a ranged for loop
    :param nums: list of integers
    :param key: integer to search for
    :return: all indexes of the key
    """
    indexes = []

    for i in range(len(nums)):
        if nums[i] is key:
            indexes.append(i)
    return indexes


def search_key_second(nums: list[int], key: int) -> list[int]:
    """
    Traversal with a standard list while loop
    :param nums: list of integers
    :param key: integer to search for
    :return: all indexes of the key
    """
    indexes = []
    length = len(nums)
    i = 0

    while i < length:
        if nums[i] is key:
            indexes.append(i)
        i += 1
    return indexes


def search_key_third(nums: list[int], key: int) -> list[int]:
    """
    Traversal with a standard list for loop
    :param nums: list of integers
    :param key: integer to search for
    :return: all indexes of the key
    """
    indexes = []
    i = 0

    for num in nums:
        if num is key:
            indexes.append(i)
        i += 1
    return indexes


def search_key_fourth(nums: list[int], key: int) -> list[int]:
    """
    Traversal with the enumerate loop
    :param nums: list of integers
    :param key: integer to search for
    :return: all indexes of the key
    """
    indexes = []

    for index, num in enumerate(nums):
        if num is key:
            indexes.append(index)
    return indexes
