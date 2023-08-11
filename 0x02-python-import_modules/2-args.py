#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]  
    count_args = len(arguments)

    print("{} argument{}:".format(count_args, "s" if count_args != 1 else ""))
    
    for position, argument in enumerate(arguments, start=1):
        print("{}: {}".format(position, argument))
