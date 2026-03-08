import json
import os

FILE_NAME = "library_data.json"


# ---------------------- Book Class ----------------------

class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued": self.issued
        }


# ---------------------- Library Class ----------------------

class Library:

    def __init__(self):
        self.books = {}
        self.load_books()

    # Load books from JSON
    def load_books(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                for book in data:
                    self.books[book["book_id"]] = Book(
                        book["book_id"],
                        book["title"],
                        book["author"],
                        book["issued"]
                    )

    # Save books to JSON
    def save_books(self):
        data = [book.to_dict() for book in self.books.values()]
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        self.books[book_id] = Book(book_id, title, author)
        self.save_books()
        print("Book added successfully!")

    # Search Book
    def search_book(self):
        keyword = input("Enter title or author to search: ").lower()

        found = False
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                status = "Issued" if book.issued else "Available"
                print(f"{book.book_id} | {book.title} | {book.author} | {status}")
                found = True

        if not found:
            print("No books found.")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        if book_id in self.books:
            book = self.books[book_id]

            if book.issued:
                print("Book already issued.")
            else:
                book.issued = True
                self.save_books()
                print("Book issued successfully.")
        else:
            print("Book not found.")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        if book_id in self.books:
            book = self.books[book_id]

            if not book.issued:
                print("Book was not issued.")
            else:
                book.issued = False
                self.save_books()
                print("Book returned successfully.")
        else:
            print("Book not found.")

    # Report
    def report(self):
        total = len(self.books)
        issued = sum(1 for book in self.books.values() if book.issued)

        print("\nLibrary Report")
        print("Total Books:", total)
        print("Issued Books:", issued)
        print("Available Books:", total - issued)


# ---------------------- Menu ----------------------

def menu():
    library = Library()

    while True:
        print("\n====== Library Inventory Manager ======")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Library Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.search_book()

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.report()

        elif choice == "6":
            print("Exiting Library Manager")
            break

        else:
            print("Invalid choice!")


# ---------------------- Run Program ----------------------

if __name__ == "__main__":
    menu()