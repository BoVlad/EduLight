import sqlite3
import bcrypt

# conn = sqlite3.connect("my_database.db")
# cursor = conn.cursor()

def all_db_start():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                      (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT UNIQUE NOT NULL,
                          email TEXT UNIQUE NOT NULL,
                          password_hash TEXT NOT NULL,
                          created_at TEXT DEFAULT CURRENT_TIMESTAMP
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS courses
                      (
                          id          INTEGER PRIMARY KEY AUTOINCREMENT,
                          title       TEXT NOT NULL,
                          description_short TEXT NOT NULL,
                          description TEXT NOT NULL,
                          img TEXT NOT NULL,
                          modules_quantity INTEGER NOT NULL
                              CHECK (modules_quantity >= 1 AND modules_quantity <= 24),
                          created_at  TEXT DEFAULT CURRENT_TIMESTAMP
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS modules
                      (
                          id          INTEGER PRIMARY KEY AUTOINCREMENT,
                          course_id INTEGER,
                          title       TEXT NOT NULL,
                          module_number INTEGER NOT NULL
                              CHECK (module_number >= 1 AND module_number <= 24),
                          FOREIGN KEY (course_id) REFERENCES courses (id)
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS lessons
                      (
                          id        INTEGER PRIMARY KEY AUTOINCREMENT,
                          course_id INTEGER,
                          module_number INTEGER,
                          title     TEXT NOT NULL,
                          content   TEXT NOT NULL,
                          module_id INTEGER NOT NULL
                              CHECK (module_id >= 1 AND module_id <= 24),
                          FOREIGN KEY (course_id) REFERENCES courses (id),
                          FOREIGN KEY (module_id) REFERENCES modules (id),
                          FOREIGN KEY (module_number) REFERENCES modules (module_number)
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_courses
                      (
                          id               INTEGER PRIMARY KEY AUTOINCREMENT,
                          user_id          INTEGER,
                          course_id        INTEGER,
                          progress_percent INTEGER DEFAULT 0,
                          started_at       TEXT    DEFAULT CURRENT_TIMESTAMP,
                          completed_at     TEXT,
                          FOREIGN KEY (user_id) REFERENCES users (id),
                          FOREIGN KEY (course_id) REFERENCES courses (id)
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS lesson_progress
                      (
                          id           INTEGER PRIMARY KEY AUTOINCREMENT,
                          user_id      INTEGER,
                          lesson_id    INTEGER,
                          is_completed INTEGER DEFAULT 0 NOT NULL
                              CHECK (is_completed IN (0,1)),
                          score        INTEGER,
                          completed_at TEXT,
                          FOREIGN KEY (user_id) REFERENCES users (id),
                          FOREIGN KEY (lesson_id) REFERENCES lessons (id)
                      );
                   """)
    conn.commit()


def get_db_conn():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def check_user_in_db(email: str, password: str):
    conn = get_db_conn()
    cursor = conn.cursor()
    email = email.lower()
    cursor.execute("SELECT password_hash FROM users WHERE email = ?", (email,))

    password_db = cursor.fetchone()
    if password_db is None:
        return None
    password_db = password_db["password_hash"]
    return bcrypt.checkpw(password.encode('utf-8'), password_db.lower())

def add_user_to_db(username: str, email: str, password: str):
    conn = get_db_conn()
    cursor = conn.cursor()
    password = password.lower()

    salt = bcrypt.gensalt()
    password_input_hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    cursor.execute("""INSERT INTO users (username, email, password_hash)
                      VALUES (?, ?, ?)""",
                   (username, email, password_input_hashed))
    conn.commit()
    conn.close()





