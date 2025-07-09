#get number of words
import sys
from stats import get_book_text
from stats import number_in_string
from stats import character_in_text
from stats import characters_sorted

def main():
    if len(sys.argv) < 2:
        # check argument before trying to use it
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    book_words = number_in_string(book_content)
    book_characters = character_in_text(book_content)
    character_report = characters_sorted(book_characters)
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for item in character_report:
       if item["char"].isalpha():
           print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
