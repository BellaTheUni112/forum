from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3, os, time
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def db():
    return sqlite3.connect('forum.db')

conn = db()
conn.execute("CREATE TABLE IF NOT EXISTS boards (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
conn.execute("CREATE TABLE IF NOT EXISTS threads (id INTEGER PRIMARY KEY, board_id INTEGER, title TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, thread_id INTEGER, name TEXT, comment TEXT, image TEXT)")
conn.execute("INSERT OR IGNORE INTO boards (name) VALUES ('b'), ('tech'), ('media'), ('random')")
conn.commit()
conn.close()

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def home():
    conn = db()
    boards = conn.execute("SELECT * FROM boards").fetchall()
    conn.close()
    return render_template('home.html', boards=boards)

@app.route('/<board>/', methods=['GET', 'POST'])
def view_board(board):
    conn = db()
    b = conn.execute("SELECT * FROM boards WHERE name=?", (board,)).fetchone()

    if not b:
        return "Board not found"

    if request.method == 'POST':
        title = request.form.get('title', 'No title')
        name = request.form.get('name', 'Anonymous')
        comment = request.form.get('comment', '')
        image_file = request.files.get('image')

        filename = ''
        if image_file and image_file.filename:
            filename = str(int(time.time())) + "_" + secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur = conn.cursor()
        cur.execute("INSERT INTO threads (board_id, title) VALUES (?, ?)", (b[0], title))
        thread_id = cur.lastrowid

        cur.execute("INSERT INTO posts (thread_id, name, comment, image) VALUES (?, ?, ?, ?)",
                    (thread_id, name, comment, filename))

        conn.commit()
        return redirect(url_for('view_board', board=board))

    threads = conn.execute("SELECT * FROM threads WHERE board_id=? ORDER BY id DESC", (b[0],)).fetchall()
    conn.close()

    return render_template('board.html', board=board, threads=threads)

@app.route('/thread/<int:thread_id>', methods=['GET', 'POST'])
def view_thread(thread_id):
    conn = db()

    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous')
        comment = request.form.get('comment', '')
        image_file = request.files.get('image')

        filename = ''
        if image_file and image_file.filename:
            filename = str(int(time.time())) + "_" + secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn.execute("INSERT INTO posts (thread_id, name, comment, image) VALUES (?, ?, ?, ?)",
                     (thread_id, name, comment, filename))
        conn.commit()
        return redirect(url_for('view_thread', thread_id=thread_id))

    posts = conn.execute("SELECT * FROM posts WHERE thread_id=?", (thread_id,)).fetchall()
    conn.close()

    return render_template('thread.html', posts=posts, thread_id=thread_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8094)
