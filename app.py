from flask import Flask, jsonify, request
from database import get_connection, init_db

app = Flask(__name__)

# Initialize DB on startup
init_db()

@app.route("/")
def home():
    return {
        "message": "Welcome to E-Learning Platform (DBaaS Demo on GitHub)",
        "routes": ["/students", "/courses", "/enrollments"]
    }

# ---------------- STUDENTS ----------------
@app.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    conn = get_connection()
    conn.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Student added!"}, 201

# ---------------- COURSES ----------------
@app.route("/courses", methods=["GET"])
def get_courses():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route("/courses", methods=["POST"])
def add_course():
    data = request.json
    conn = get_connection()
    conn.execute(
        "INSERT INTO courses (title, description) VALUES (?, ?)",
        (data["title"], data["description"])
    )
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Course added!"}, 201

# ---------------- ENROLLMENTS ----------------
@app.route("/enrollments", methods=["GET"])
def get_enrollments():
    conn = get_connection()
    query = """
        SELECT e.id, s.name AS student, c.title AS course
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
    """
    rows = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route("/enrollments", methods=["POST"])
def add_enrollment():
    data = request.json
    conn = get_connection()
    conn.execute(
        "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
        (data["student_id"], data["course_id"])
    )
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Enrollment added!"}, 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
