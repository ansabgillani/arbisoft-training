import matplotlib.pyplot as plt

from utils.utils import (
    generate_random_dictionary,
    generate_random_string,
    calculate_execution_time,
)

from appending_random_string import (
    append_random_string_items,
    append_random_string_keys,
    append_random_string_comprehension
)

if __name__ == "__main__":

    flag = 1

    while flag:
        # input number of elements
        size_n = int(input("Enter the number of elements in the dictionary: "))

        # generating a random dictionary
        random_dict = generate_random_dictionary(size_n)

        # generating a random string
        random_string = generate_random_string(5)

        # calculating execution time of dictionary comprehension
        comprehension_exec_time = calculate_execution_time(append_random_string_comprehension,
                                                           dictionary=random_dict, random_string=random_string)
        print(f"Time taken to for the "
              f"comprehension : {comprehension_exec_time}")

        # calculating execution time of dictionary.items()
        items_exec_time = calculate_execution_time(append_random_string_items,
                                                   dictionary=random_dict, random_string=random_string)
        print(f"Time taken to for the "
              f"items loop : {items_exec_time}")

        # calculating execution time of dictionary.keys()
        keys_exec_time = calculate_execution_time(append_random_string_keys,
                                                  dictionary=random_dict, random_string=random_string)
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
