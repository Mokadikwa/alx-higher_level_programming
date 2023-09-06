#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':' characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    newline_flag = False

    for char in text:
        if char not in "?:.":
            if newline_flag:
                result += "\n\n"
                newline_flag = False
            result += char
        else:
            result += char
            newline_flag = True

    print(result.strip())
