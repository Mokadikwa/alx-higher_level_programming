#!/usr/bin/python3
def text_indentation(text):
    """Prints text with new lines after specified characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for char in text:
        result += char

        if char in ".?:":
            result += "\n\n"

    print(result.strip())
