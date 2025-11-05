from stats import get_num_words
from stats import characters
from stats import sort_characters

def main():
    result = characters("books/frankenstein.txt")
    sorted_list = sort_characters("books/frankenstein.txt")
    
    print("============ BOOKBOT ===========\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {get_num_words("books/frankenstein.txt")} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")
main()
