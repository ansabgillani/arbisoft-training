import time
import random as rnd

import matplotlib.pyplot as plt

from index_search import (
    search_key_while,
    search_key_enumerate,
    search_key_listed_for,
    search_key_ranged_for,
    search_key_comprehension
)

if __name__ == "__main__":

    def calculate_execution_time(function):
        start = time.time()
        function(nums, key)
        end = time.time()
        execution_time = end - start
        return execution_time

    while True:

        # input number of elements
        size_n = int(input("Enter the number of elements in the list: "))

        nums = [rnd.randrange(1, 100) for i in range(size_n)]

        # Asking for the key to be searched
        key = int(input("Enter the number "
                        "you want to search : "))

        # Calculating Execution of while loop
        while_exec_time = calculate_execution_time(search_key_while)
        print(f"Time taken to for the "
              f"while loop : {while_exec_time}")

        # Calculating Execution of enumerate loop
        enumerate_exec_time = calculate_execution_time(search_key_enumerate)
        print(f"Time taken to for the "
              f"enumerate loop : {enumerate_exec_time}")

        # Calculating Execution of listed for loop
        for_exec_time = calculate_execution_time(search_key_listed_for)
        print(f"Time taken to for the "
              f"listed for loop : {for_exec_time}")

        # Calculating Execution of ranged for loop
        range_exec_time = calculate_execution_time(search_key_ranged_for)
        print(f"Time taken to for the "
              f"ranged for loop : {range_exec_time}")

        # Calculating Execution of while loop
        comprehension_exec_time = calculate_execution_time(search_key_comprehension)
        print(f"Time taken to for the "
              f"list comprehension : {comprehension_exec_time}")

        x_axis = ['While',
                  'Enumerate',
                  'Listed For',
                  'Range',
                  'List Comprehension']
        y_axis = [while_exec_time,
                  enumerate_exec_time,
                  for_exec_time,
                  range_exec_time,
                  comprehension_exec_time]

        plt.title(f'Input Size: {size_n}')
        plt.bar(x_axis, y_axis)
        plt.show()

        ex = int(input("Press 0 to exit or "
                       "any other key to continue: "))
        if ex == 0:
            break
