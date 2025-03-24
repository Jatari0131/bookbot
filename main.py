import sys

#define get_book_text outside of main
def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    from stats import get_num_words, char_count, sort_characters

    # Ensure correct usage

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path and read contents

    book_path = sys.argv[1]
    with open(book_path, 'r') as book:
        text = book.read()

    # Compute book stats
    num_words = get_num_words(text)
    char_dict = char_count(text)
    sorted_dict = sort_characters(char_dict)

    # Print the results
    print(f"Found {num_words} total words")
    for char_info in sorted_dict:
        print(f"{char_info['char']}: {char_info['count']}")  


main()
