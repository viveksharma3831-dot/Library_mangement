from utils import issued_books


def show_issued_books():
    print("\nIssued Books")
    if len(issued_books) == 0:
        print("No issued books")
    else:
        for book_name, details in issued_books.items():
            print(book_name, "issued to", details["student_name"], "due on", details["due_date"])
