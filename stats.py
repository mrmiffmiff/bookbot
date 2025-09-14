def get_book_word_count(book_text):
    text_list = book_text.split()
    return len(text_list)

def get_book_char_counts(book_text):
    lower_book_text = book_text.lower()
    char_counts = {}
    for char in lower_book_text:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts

# Helper for sort_chars
def sort_helper(char_dict):
    return char_dict["num"]

def sort_chars(chars_with_counts):
    sorted_chars = []
    for char in chars_with_counts:
        char_dict = {"char": char, "num": chars_with_counts[char]}
        sorted_chars.append(char_dict)
    sorted_chars.sort(key=sort_helper, reverse=True)
    return sorted_chars