#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a * b - c

    result = magic_calculation(-1, 0, 3)
    print(result)
