#!/usr/bin/python3

def append_write(filename="", text=""):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
