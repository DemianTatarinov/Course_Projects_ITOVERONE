import sqlite3
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1
    (book_id INT PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT,
    year YEAR(2018))
    ''')
# cursor.execute('''INSERT info tab_1(title,author,price,amount,year) VALUES(?,?,?,?,?)''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
a = cursor.fetchall()
print(a)
# for i in a:
#     i = list(i)
#     h = 0
#     print(''.join(str(h) for h in i))