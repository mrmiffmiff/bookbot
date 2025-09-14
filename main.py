from stats import get_book_word_count, get_book_char_counts, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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