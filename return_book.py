from datetime import date
from utils import books, issued_books, calculate_fine


def return_book():
    book_name = input("Enter book name to return: ").strip().title()

    if book_name not in issued_books:
        print("Book was not issued")
        return

    due_date = date.fromisoformat(issued_books[book_name]["due_date"])
    today = date.today()
    late_days = (today - due_date).days

    if book_name in books:
        books[book_name] = books[book_name] + 1
    else:
        books[book_name] = 1

    student_name = issued_books[book_name]["student_name"]
    del issued_books[book_name]

    print("Book returned successfully by", student_name)

    if late_days > 0:
        fine = calculate_fine(late_days)
        print("Late by", late_days, "days")
        print("Fine is Rs", fine)
    else:
        print("Returned within time. No fine")
