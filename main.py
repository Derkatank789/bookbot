def get_book_text(path):
    with open(path) as f:
        file = f.read()
    return file
def count_word(file):
    f = get_book_text(file)
    return len(f.split())

def main():
    print(f"{count_word("books/frankenstein.txt")} words found in the document")
    return

main()