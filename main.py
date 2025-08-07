from stats import count_words, character_count, print_a_report

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = count_words(result)
    print(f"Found {num_words} total words")

    char_counts = character_count(result)

    report = print_a_report(char_counts)
    
    for item in report:
        print(f"{item['char']}: {item['num']}")



if __name__ == "__main__":
    main()
