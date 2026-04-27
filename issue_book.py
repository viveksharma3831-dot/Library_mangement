from datetime import date, timedelta
from utils import books, issued_books


def issue_book():
    book_name = input("Enter book name to issue: ").strip().title()

    if book_name not in books or books[book_name] == 0:
        print("Book not available")
        return

    student_name = input("Enter student name: ").strip().title()
    days = input("Enter number of days: ")

    if student_name == "":
        print("Student name cannot be empty")
        return

    if not days.isdigit():
        print("Enter valid number of days")
        return

    days = int(days)
    issue_date = date.today()
    due_date = issue_date + timedelta(days=days)

    books[book_name] = books[book_name] - 1
    issued_books[book_name] = {
        "student_name": student_name,
        "issue_date": str(issue_date),
        "days": days,
        "due_date": str(due_date)
    }

    print("Book issued successfully")
    print("Issue Date:", issue_date)
    print("Due Date:", due_date)
    print("Fine Rule:")
    print("1 week - 10 Rs/day/book")
    print("2nd week - 20 Rs/day/book")
    print("3rd week - 60 Rs/day/book")
