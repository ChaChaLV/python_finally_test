import sqlite3 as sl


conn = sl.connect("phonebook.bd")

cur = conn.cursor()


def load_database():
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
                )
                """
            )

    cur.execute("""
                CREATE TABLE IF NOT EXISTS numbers
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEJER,
                user_id INTEJER,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                )
                """
            )

    cur.execute("""
                CREATE TABLE IF NOT EXISTS email
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                user_id INTEJER,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                )
                """
            )
    conn.commit()
    

def add_contact(contact_info): 
    name, number, extra_number, email = contact_info
    
    cur.execute("INSERT INTO users (name) VALUES (?);", (name,)) 
    user_id = cur.lastrowid 
    
    cur.execute("INSERT INTO numbers (number, user_id) VALUES (?, ?);", (number, user_id)) 
    if extra_number: 
        cur.execute("INSERT INTO numbers (number, user_id) VALUES (?, ?);", (extra_number, user_id)) 
    cur.execute("INSERT INTO email (email, user_id) VALUES (?, ?);", (email, user_id)) 
    
    conn.commit()


def view_contacts():
    cur.execute("""
        SELECT users.name, numbers.number, email.email
        FROM users 
        LEFT JOIN numbers ON users.id = numbers.user_id 
        LEFT JOIN email ON users.id = email.user_id
    """)
    for result in cur.fetchall():
        print(result)


def search_contact (name):
    cur.execute("""
        SELECT users.name, numbers.number, email.email
        FROM users 
        LEFT JOIN numbers ON users.id = numbers.user_id 
        LEFT JOIN email ON users.id = email.user_id
        WHERE users.name = ?
    """, (name,))

    results = cur.fetchall()
    if results:
        for result in results:
            print(result)
    else:
        print("Контакт не найден.")


def delete_contact(name):
    cur.execute("SELECT id FROM users WHERE name = ?", (name,))
    result = cur.fetchone()
    if result:
        user_id = result[0]
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        print(f"Контакт '{name}' и все связанные данные были успешно удалены.")
    else:
        print("Контакт не найден.")
    conn.commit()


def update_contact(name, contact_info): 
    number, email = contact_info
    cur.execute("SELECT id FROM users WHERE name = ?", (name,)) 
    result = cur.fetchone() 
    if result: 
        user_id = result[0] 
        cur.execute("UPDATE numbers SET number = ? WHERE user_id = ?;", (number, user_id)) 
        cur.execute("UPDATE email SET email = ? WHERE user_id = ?;", (email, user_id)) 
        print(f"Контакт '{name}' успешно изменён.") 
    else: 
        print("Контакт не найден.")  
    conn.commit()


