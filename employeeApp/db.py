import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, first_name text, last_name text, phone text, email text)")
        self.conn.commit()
        
    def get(self):
        self.cur.execute("SELECT * FROM employees")
        rows= self.cur.fetchall()
        return rows
    
    def set(self, first_name, last_name, phone, email):
        self.cur.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?)", (first_name, last_name, phone, email))
        self.conn.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()
        
    def update(self, id, first_name, last_name, phone, email):
        self.cur.execute("UPDATE employees SET first_name = ?, last_name = ?, phone = ?, email = ? WHERE id = ?", (first_name, last_name, phone, email, id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
        
#db = Database('employee.db')

#db.set("Jon", "Jones", "12345678", "test@gmail.com")