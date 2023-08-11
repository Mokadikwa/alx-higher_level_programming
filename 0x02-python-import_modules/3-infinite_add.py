#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    total_sum = 0

    for argument in arguments:
        total_sum += int(argument)

    print("{}".format(total_sum))
