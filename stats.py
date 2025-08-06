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
