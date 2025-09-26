from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('elearning.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "E-Learning Platform DBaaS Demo (GitHub Only)"

@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return jsonify([dict(row) for row in students])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
