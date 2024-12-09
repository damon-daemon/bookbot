import string

def sort_on(char_dict):
    return char_dict["count"]

def char_count(book: str) -> None:
    book = book.lower()
    char_list = []
    alpha_list = list("abcdefghijklmnopqrstuvwxyz")
    
    for alpha in alpha_list:
        char_dict = {}
        alpha_count = book.count(alpha)
        char_dict["char"] = alpha
        char_dict["count"] = alpha_count
        char_list.append(char_dict)
    
    sorted_char_list = sorted(char_list, key=sort_on, reverse=True)
    
    word_count = len(book.split())
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for char in sorted_char_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    
    print("--- End report ---")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    char_count(file_contents)
