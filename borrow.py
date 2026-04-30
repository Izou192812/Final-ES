class BorrowManagement:

    def borrow_book(self, member, book):
        if book.quantity <= 0:
            print("Hết sách")
            return None

        book.quantity -= 1

        borrow = {
            "member": member,
            "book": book,
            "penalty": 0
        }

        print("Mượn thành công")
        return borrow


    def calculate_penalty(self, late_days):
        if late_days > 0:
            return late_days * 5000
        return 0


    def return_book(self, borrow):
        late_days = int(input("Nhập số ngày trễ: "))

        borrow["penalty"] = self.calculate_penalty(late_days)
        borrow["book"].quantity += 1

        print("Trả sách xong")
        print("Tiền phạt:", borrow["penalty"])