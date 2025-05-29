from stats import get_num_words
from stats import get_num_of_each_character

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main ():
    file_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(file_contents)

    print(f"{num_words} words found in the document")

    num_of_each_char = get_num_of_each_character(file_contents)

    print(num_of_each_char)

main()
