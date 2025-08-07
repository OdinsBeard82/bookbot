def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}  # Empty dictionary
    characters = text.lower()   # Converts string to lower case
    for char in characters:  # Loop through lower case string
        if char in char_count:
            char_count[char] += 1 # If it’s already in the dictionary, count +1
        else:
            char_count[char] = 1 # If it’s not in the dictionary, count + 1
    return char_count # Return the dictionary

def print_a_report(char_count):
    sorted_list = []  # Empty list to store dictionaries of characters and counts

    for char, count in char_count.items():  # Loop through the dictionary
        if not char.isalpha():  # Skip characters that are not letters
            continue
        sorted_list.append({"char": char, "num": count})  # Add a dictionary with char and count

    sorted_list.sort(key=lambda d: d["num"], reverse=True)  # Sort list from greatest to least by count
    return sorted_list  # Return the sorted list


