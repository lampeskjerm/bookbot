import sys
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import sort_characters

def main():
    sorted_list = sort_characters(sys.argv[1])
    
    print(f"============ BOOKBOT ===========\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f"Found {get_num_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

main()
