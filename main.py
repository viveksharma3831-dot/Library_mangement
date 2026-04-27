from add_book import add_book
from show_books import show_books
from issue_book import issue_book
from show_issued_books import show_issued_books
from return_book import return_book


def library_menu():
    while True:
        print("\n----- LIBRARY MENU -----")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Show Issued Books")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            show_issued_books()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you")
            break
        else:
            print("Invalid choice")


library_menu()
