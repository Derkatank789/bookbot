def get_book_text(path):
    with open(path) as f:
        file = f.read()
    return file


def main():
    print(get_book_text("books/frankenstein.txt"))
    return

main()