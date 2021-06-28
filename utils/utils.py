import random
import string
import time


def generate_random_dictionary(size: int) -> dict:
    """
    Helper function that generates a random dictionary
    with random keys and random values
    :param size: size of the required dictionary
    :return: the dictionary object
    """
    rand_dict = dict()

    for i in range(size):
        key = generate_random_string(5)
        value = generate_random_string(5)
        rand_dict[key] = value

    return rand_dict


def generate_random_string(size: int) -> str:
    """
    Helper function that generates a random string
    :param size: size of the required string
    :return: the string object
    """
    return ''.join(random.choice(string.digits + string.ascii_uppercase) for x in range(size))


def calculate_execution_time(function, **kwargs):
    """
    Helper function to calculate execution time of any function
    :param function: the function you want to run
    :param kwargs: arguments for the function
    :return: execution time
    """
    start = time.time()
    function(**kwargs)
    end = time.time()
    execution_time = end - start
    return execution_time
