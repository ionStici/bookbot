from stats import get_num_words
from stats import get_num_of_each_character
from stats import get_sorted_dict
import sys

env_vars = sys.argv
is_env_valid = len(env_vars) > 1

if not is_env_valid :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()

filepath = env_vars[1]

def main ():
    file_contents = get_book_text(filepath)
    num_words = get_num_words(file_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    num_of_each_char = get_num_of_each_character(file_contents)
    sorted_list = get_sorted_dict(num_of_each_char)

    for item in sorted_list:
        if (item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()
