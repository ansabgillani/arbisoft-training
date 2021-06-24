
import index_search as test
import time
import matplotlib.pyplot as plt
import random as rnd

if __name__ == "__main__":

    while True:

        flag_random = int(input("Do you want a randomized integer list?\n"
                                "Press 0 to generate or 1 for user input "))

        nums = []

        if flag_random == 0:
            # input number of elements
            n = int(input("Enter the number of elements in the list: "))

            nums = [rnd.randrange(1, 50) for i in range(n)]
            print(nums)

        else:
            # Below line read inputs from user using map() function
            nums = list(map(int,
                            input("Enter the numbers : ").strip().split()))

        # Asking for the key to be searched
        key = int(input("Enter the number "
                        "you want to search : "))

        # Calculating Execution of first loop
        start = time.time()
        print(test.search_key_first(nums, key=key))
        end = time.time()
        first_exec_time = end - start
        print(f"Time taken to for the "
              f"first loop : {first_exec_time}")

        # Calculating Execution of second loop
        start = time.time()
        print(test.search_key_second(nums, key=key))
        end = time.time()
        second_exec_time = end - start
        print(f"Time taken to for the "
              f"second loop : {second_exec_time}")

        # Calculating Execution of third loop
        start = time.time()
        print(test.search_key_third(nums, key=key))
        end = time.time()
        third_execution_time = end - start
        print(f"Time taken to for the "
              f"third loop : {third_execution_time}")

        # Calculating Execution of fourth loop
        start = time.time()
        print(test.search_key_fourth(nums, key=key))
        end = time.time()
        fourth_execution_time = end - start
        print(f"Time taken to for the "
              f"fourth loop : {fourth_execution_time}")

        x_axis = ['Ranged for Loop',
                  'While Loop',
                  'Listed for loop',
                  'Enumerated Loop']
        y_axis = [first_exec_time,
                  second_exec_time,
                  third_execution_time,
                  fourth_execution_time]

        plt.bar(x_axis, y_axis)
        plt.show()

        ex = int(input("Press 0 to exit or "
                       "any other key to continue: "))
        if ex == 0:
            break
