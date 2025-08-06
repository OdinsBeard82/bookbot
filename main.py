from stats import count_words, character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = count_words(result)
    print(f"{num_words} words found in the document")

    char_counts = character_count(result)
    print(char_counts)

if __name__ == "__main__":
    main()
