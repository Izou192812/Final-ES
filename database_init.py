import sqlite3
from datetime import datetime, timedelta
#Hàm kết nối Database 
def get_connection():
    return sqlite3.connect('library.db')
#Khởi tạo các bảng dữ liệu 
def init_db():
    conn = get_connection()
    cursor = conn.cursor()    
#Tạo bảng Thành viên
    cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
        Member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Full_name TEXT, Email TEXT UNIQUE, Password TEXT, Role TEXT)''')  
#Tạo bảng Sách
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
        Book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT, Author TEXT, Category TEXT, Quantity INTEGER)''')   
#Tạo bảng Mượn trả
    cursor.execute('''CREATE TABLE IF NOT EXISTS Borrow (
        Borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Member_id INTEGER, Book_id INTEGER,
        Borrow_date TEXT, Due_date TEXT, Return_date TEXT,
        Status TEXT, Penalty REAL DEFAULT 0)''') 
#Thêm dữ liệu mẫu để chạy thử
    try:
        cursor.execute("INSERT INTO Members (Full_name, Email, Password, Role) VALUES ('Tran Truong Hai', 'hai@uth.edu.vn', '123', 'Admin')")
        cursor.execute("INSERT INTO Books (Title, Author, Category, Quantity) VALUES ('Software Engineering', 'Pressman', 'Technical', 5)")
        conn.commit()
    except:
        pass #Nếu đã có dữ liệu rồi thì bỏ qua 
    conn.close()
#Hàm mượn sách
def borrow_book(member_id, book_id):
    conn = get_connection()
    cursor = conn.cursor()  
    cursor.execute("SELECT Quantity FROM Books WHERE Book_id = ?", (book_id,))
    res = cursor.fetchone()
    if res and res[0] > 0:
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=7)    
        cursor.execute("INSERT INTO Borrow (Member_id, Book_id, Borrow_date, Due_date, Status) VALUES (?, ?, ?, ?, 'Borrowing')",
                       (member_id, book_id, str(borrow_date), str(due_date)))
        cursor.execute("UPDATE Books SET Quantity = Quantity - 1 WHERE Book_id = ?", (book_id,))
        conn.commit()
        print(">>> Mượn sách thành công!")
    else:
        print(">>> Sách đã hết hoặc không tồn tại!")
    conn.close()
#Chương trình chính
if __name__ == "__main__":
    init_db()
    print("--- HỆ THỐNG QUẢN LÝ THƯ VIỆN UTH ---")
    print("1. Chạy thử chức năng mượn sách")
    #Mượn sách ID 1 cho Thành viên ID 1
    borrow_book(1, 1)
    #Kiểm tra kết quả trong Database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    print("Danh sách sách hiện tại:", cursor.fetchall())
    conn.close()
