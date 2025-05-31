def get_book_text(book):
    text = ""
    with open(book) as f:
        text = f.read()
    return text

def main():
    booktext = get_book_text("books/frankenstein.txt")
    print(booktext)

main()

