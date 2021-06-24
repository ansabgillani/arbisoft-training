import index_search as test
import time
import matplotlib.pyplot as plt
import random as rnd

if __name__ == "__main__":

    while True:

        # input number of elements
        size_n = int(input("Enter the number of elements in the list: "))

        nums = [rnd.randrange(1, 100) for i in range(size_n)]

        # Asking for the key to be searched
        key = int(input("Enter the number "
                        "you want to search : "))

        # Calculating Execution of first loop
        start = time.time()
        test.search_key_first(nums, key=key)
        end = time.time()
        first_exec_time = end - start
        print(f"Time taken to for the "
              f"first loop : {first_exec_time}")

        # Calculating Execution of second loop
        start = time.time()
        test.search_key_second(nums, key=key)
        end = time.time()
        second_exec_time = end - start
        print(f"Time taken to for the "
              f"second loop : {second_exec_time}")

        # Calculating Execution of third loop
        start = time.time()
        test.search_key_third(nums, key=key)
        end = time.time()
        third_execution_time = end - start
        print(f"Time taken to for the "
              f"third loop : {third_execution_time}")

        # Calculating Execution of fourth loop
        start = time.time()
        test.search_key_fourth(nums, key=key)
        end = time.time()
        fourth_execution_time = end - start
        print(f"Time taken to for the "
              f"fourth loop : {fourth_execution_time}")

        # Calculating Execution of list comprehension
        start = time.time()
        test.search_key_fifth(nums, key=key)
        end = time.time()
        fifth_execution_time = end - start
        print(f"Time taken to for the "
              f"fifth loop : {fifth_execution_time}")

        x_axis = ['Ranged for',
                  'While',
                  'Listed for',
                  'Enumerated',
                  'List Comprehension']
        y_axis = [first_exec_time,
                  second_exec_time,
                  third_execution_time,
                  fourth_execution_time,
                  fifth_execution_time]

        plt.title(f'Input Size: {size_n}')
        plt.bar(x_axis, y_axis)
        plt.show()

        ex = int(input("Press 0 to exit or "
                       "any other key to continue: "))
        if ex == 0:
            break
