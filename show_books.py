from utils import books


def show_books():
    print("\nAvailable Books")
    if len(books) == 0:
        print("No books available")
    else:
        for book_name, quantity in books.items():
            print(book_name, "- Copies:", quantity)
