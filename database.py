import sqlite3

DB_NAME = "elearning.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    with open("schema.sql") as f:
        conn.executescript(f.read())
    with open("sample_data.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
