import string
import random
import time

import matplotlib.pyplot as plt

from appending_random_string import (
    append_random_string_items,
    append_random_string_keys,
    append_random_string_comprehension
)


def generate_random_dictionary(size: int) -> dict:
    """
    Helper function that generates a random dictionary
    with random keys and random values
    :param size: size of the required dictionary
    :return: the dictionary object
    """
    rand_dict = dict()

    for i in range(size):
        key = ''.join(random.choice(string.digits + string.ascii_uppercase) for x in range(5))
        value = ''.join(random.choice(string.digits + string.ascii_uppercase) for x in range(5))
        rand_dict[key] = value

    return rand_dict


if __name__ == "__main__":

    def calculate_execution_time(function):
        """
        Helper function that calculates the
        execution time of a function.
        :param function: function that you want to run.
        :return: None
        """
        start = time.time()
        function(random_dict, random_string)
        end = time.time()
        execution_time = end - start
        return execution_time


    flag = 1

    while flag:
        # input number of elements
        size_n = int(input("Enter the number of elements in the dictionary: "))

        # generating a random dictionary
        random_dict = generate_random_dictionary(size_n)

        # generating a random string
        random_string = ''.join(random.choice(string.digits + string.ascii_uppercase) for x in range(3))

        # calculating execution time of dictionary comprehension
        comprehension_exec_time = calculate_execution_time(append_random_string_comprehension)
        print(f"Time taken to for the "
              f"comprehension : {comprehension_exec_time}")

        # calculating execution time of dictionary.items()
        items_exec_time = calculate_execution_time(append_random_string_items)
        print(f"Time taken to for the "
              f"items loop : {items_exec_time}")

        # calculating execution time of dictionary.keys()
        keys_exec_time = calculate_execution_time(append_random_string_keys)
        print(f"Time taken to for the "
              f"keys loop : {keys_exec_time}")

        x_axis = [
            'Comprehension',
            'items',
            'Keys'
            ]
        y_axis = [
            comprehension_exec_time,
            items_exec_time,
            keys_exec_time
            ]

        plt.title(f'Input Size: {size_n}')
        plt.bar(x_axis, y_axis)
        plt.show()

        ex = int(input("Press 0 to exit or "
                       "any other key to continue: "))
        if ex == 0:
            break
