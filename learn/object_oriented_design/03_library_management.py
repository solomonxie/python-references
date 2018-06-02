"""
OOD: Library Management System.
Books have multiple copies; members check out and return copies, with a
cap on how many a member may hold at once.
"""
from datetime import datetime, timedelta


class Book:
    def __init__(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies


class Member:
    def __init__(self, member_id, name, max_books=3):
        self.member_id = member_id
        self.name = name
        self.max_books = max_books
        self.checked_out = {}


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def checkout(self, member_id, isbn, loan_days=14):
        member = self.members[member_id]
        book = self.books[isbn]
        if len(member.checked_out) >= member.max_books:
            raise ValueError(f"{member.name} has reached the checkout limit")
        if book.available_copies <= 0:
            raise ValueError(f"No copies of '{book.title}' available")
        book.available_copies -= 1
        due = datetime.now() + timedelta(days=loan_days)
        member.checked_out[isbn] = due
        return due

    def return_book(self, member_id, isbn):
        member = self.members[member_id]
        book = self.books[isbn]
        member.checked_out.pop(isbn, None)
        book.available_copies = min(book.total_copies, book.available_copies + 1)


if __name__ == "__main__":
    library = Library()
    library.add_book(Book("978-0", "Clean Code", "R. Martin", copies=1))
    library.register_member(Member("m1", "Alice"))

    due = library.checkout("m1", "978-0")
    print(f"Checked out, due {due.date()}")
    try:
        library.checkout("m1", "978-0")
    except ValueError as e:
        print(f"Second checkout failed: {e}")

    library.return_book("m1", "978-0")
    print(f"Available copies after return: {library.books['978-0'].available_copies}")
