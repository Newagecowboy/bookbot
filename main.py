
import sys
from stats import count_words, count_characters  
from stats import sort_dictionary


def get_book_text(file_path):
     with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    print("============ BOOKBOT ============") 
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")

    text = get_book_text(file_path)
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f" Found {word_count} total words")
    char_counts = count_characters(text)
    sorted_char_list = sort_dictionary(char_counts)
    print("--------- Character Count -------")
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        # print the report line for this character and count
    print("============= END ===============")

main()