#!/usr/bin/python3

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
    text (string): The text to print.
    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    space = True
    for char in text:
        if char in ('.', '?', ':'):
            result += char + '\n\n'
            space = True
        elif char == ' ' and space:
            continue
        else:
            result += char
            space = False

    print(result)
