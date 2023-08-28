#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
            except IndexError:
                element_1 = 0

            try:
                element_2 = my_list_2[i]
            except IndexError:
                element_2 = 0

            try:
                result = element_1 / element_2
                new_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
    except TypeError:
        print("out of range")

    return new_list
