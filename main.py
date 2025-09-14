import sys
from stats import get_book_word_count, get_book_char_counts, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    word_count = get_book_word_count(contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_counts = get_book_char_counts(contents)
    sorted_chars = sort_chars(char_counts)
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if not char_dict["char"].isalpha():
            continue
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()