from datetime import datetime, timedelta

class BorrowManagement:
    def borrow_book(self, member, book):
        if book.quantity <= 0:
            print("Hết sách")
            return None

        book.quantity -= 1

        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=7)

        print("Mượn thành công")
        return {
            "member": member,
            "book": book,
            "borrow_date": borrow_date,
            "due_date": due_date,
            "return_date": None,
            "penalty": 0
        }

    def return_book(self, borrow):
        borrow["return_date"] = datetime.now()

        # tính tiền phạt
        if borrow["return_date"] > borrow["due_date"]:
            late_days = (borrow["return_date"] - borrow["due_date"]).days
            borrow["penalty"] = late_days * 5000

        borrow["book"].quantity += 1

        print("Trả sách xong")
        print("Tiền phạt:", borrow["penalty"])