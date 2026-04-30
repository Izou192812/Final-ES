from models import Book, Member
from borrow import BorrowManagement

book = Book(1, "Python", "John", 1)
member = Member(1, "Phong", "phong@gmail.com")

bm = BorrowManagement()

borrow = bm.borrow_book(member, book)

if borrow:
    bm.return_book(borrow)