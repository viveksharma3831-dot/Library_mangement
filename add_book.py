from utils import books


def add_book():
    book_name = input("Enter book name: ").strip().title()

    if book_name == "":
        print("Book name cannot be empty")
        return

    if book_name in books:
        books[book_name] = books[book_name] + 1
    else:
        books[book_name] = 1

    print("Book added successfully")
