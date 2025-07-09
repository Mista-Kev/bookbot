# return .txt as string
def get_book_text(path):
    with open(path) as text_file:
        file_contents = text_file.read()
    return file_contents

# get number of words from a text
def number_in_string(text):
    words = text.split()
    #for word in words:
       # word_count += 1 the harder less efficenet way
    return len(words)

# get count of unique characters
def character_in_text(book_text):
    unique_character = {}
    lower_text = book_text.lower()
    for character in lower_text:
        if character in unique_character:
            unique_character[character] += 1
        else:
            unique_character[character] = 1
    return unique_character

# format report output
def sort_on(items):
    return items["num"]

# format dictionary to sort dict
def characters_sorted(character_dict):
    char_list = []
    # Loop through each character (key) and its count (value) in the dictionary
    for char, count in character_dict.items():
        # Create a new dictionary for each character with its count
        new_dict = {"char": char, "num": count}
        # Add this dictionary to our list
        char_list.append(new_dict)
    # Sort the list of dictionaries by the "num" value, largest first
    char_list.sort(reverse=True, key=sort_on)
    return char_list
