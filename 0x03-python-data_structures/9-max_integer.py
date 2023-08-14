#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = my_list[:]

    new_list.sort()

    if not new_list:
        return None
    else:
        return new_list[-1]
