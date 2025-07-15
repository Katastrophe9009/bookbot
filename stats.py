def get_word_count(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
