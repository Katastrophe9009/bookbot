from stats import get_word_count
from stats import get_char_count
filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
def main():
    book_text = get_book_text(filepath)
    char_count = get_char_count(book_text)
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")
    print(char_count)

main()