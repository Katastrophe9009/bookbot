import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    
    book_text = get_book_text(filepath)
    char_count = get_char_count(book_text)
    num_words = get_word_count(book_text)
    sorted_list = get_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dictionary in sorted_list:
        character = char_dictionary["char"]
        number = char_dictionary["num"]
        if character.isalpha():
            print(f"{character}: {number}")
    print("============= END ===============")

main()