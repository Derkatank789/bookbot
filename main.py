from stats import count_word, symbol_count, dic_sort
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file = sys.argv[1]
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_word(file)} total words")
    print("--------- Character Count -------")
    list = dic_sort(file)
    for i in list:
        print(f"{i["char"]}: {i["num"]} ")
    return

main()