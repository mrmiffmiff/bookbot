def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_book_word_count(book_text):
    text_list = book_text.split()
    return len(text_list)

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = get_book_word_count(contents)
    print(f"{word_count} words found in the document")

main()