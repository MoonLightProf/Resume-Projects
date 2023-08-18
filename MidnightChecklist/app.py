from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'todo.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_description TEXT,
            completed BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task(task_name, task_description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task_name, task_description) VALUES (?, ?)', (task_name, task_description))
    conn.commit()
    conn.close()


def update_task_completion(task_id, completed):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()


initialize_database()


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/todo")
def todo():
    tasks = get_all_tasks()
    return render_template('todolistapp.html', tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task_route():
    task_name = request.form.get("task_name")
    task_description = request.form.get("task_description")
    add_task(task_name, task_description)
    return jsonify(success=True)


@app.route("/update_task_completion", methods=["POST"])
def update_task_completion_route():
    task_id = request.form.get("task_id")
    completed = request.form.get("completed") == "true"
    update_task_completion(task_id, completed)
    return jsonify(success=True)


@app.route("/delete_task", methods=["POST"])
def delete_task_route():
    task_id = request.form.get("task_id")
    delete_task(task_id)
    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)




