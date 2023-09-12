#!/usr/bin/python3

def append_write(filename="", text=""):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            characters_added = file.write(text)
            return characters_added
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
