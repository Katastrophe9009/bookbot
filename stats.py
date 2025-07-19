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

def sort_on(dictionary):
        return dictionary["num"]

def get_sorted_list(char_count):
    sorted_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on) 
    return sorted_list

