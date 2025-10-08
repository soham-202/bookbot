import sys
from stats import (
    get_num_words, 
    get_char_dict, 
    char_dict_to_sorted_list
)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_count = get_char_dict(text)
        sorted_char_count = char_dict_to_sorted_list(char_count)
        print_report(book_path, num_words, sorted_char_count)
    
def print_report(book_path, num_words, sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")
    
    
if __name__ == "__main__":
    main()