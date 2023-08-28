#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except (IndexError, TypeError):
        for i in my_list:
            print("{}".format(i), end="")
            x += 1
        print()
        return x
