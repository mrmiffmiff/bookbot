from stats import get_book_word_count, get_book_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = get_book_word_count(contents)
    print(f"{word_count} words found in the document")
    char_counts = get_book_char_counts(contents)
    print(char_counts)

main()