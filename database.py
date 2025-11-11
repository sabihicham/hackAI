import sqlite3

def init_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(role, content):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages(role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("SELECT role, content FROM messages")
    data = c.fetchall()
    conn.close()
    return data

init_db()
