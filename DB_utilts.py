import sqlite3

# conn = sqlite3.connect("my_database.db")
# cursor = conn.cursor()

def all_db_start():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users IF NOT EXISTS
                      (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT UNIQUE NOT NULL,
                          email TEXT UNIQUE,
                          password_hash TEXT NOT NULL,
                          created_at TEXT DEFAULT CURRENT_TIMESTAMP
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE courses IF NOT EXISTS
                      (
                          id          INTEGER PRIMARY KEY AUTOINCREMENT,
                          title       TEXT NOT NULL,
                          description TEXT,
                          created_at  TEXT DEFAULT CURRENT_TIMESTAMP
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE lessons IF NOT EXISTS
                      (
                          id        INTEGER PRIMARY KEY AUTOINCREMENT,
                          course_id INTEGER,
                          title     TEXT NOT NULL,
                          content   TEXT,
                          position  INTEGER,
                          FOREIGN KEY (course_id) REFERENCES courses (id)
                      );
                   """)
    conn.commit()
    cursor.execute("""CREATE TABLE user_courses IF NOT EXISTS
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
    cursor.execute("""CREATE TABLE lesson_progress
                      (
                          id           INTEGER PRIMARY KEY AUTOINCREMENT,
                          user_id      INTEGER,
                          lesson_id    INTEGER,
                          is_completed INTEGER DEFAULT 0,
                          score        INTEGER,
                          completed_at TEXT,
                          FOREIGN KEY (user_id) REFERENCES users (id),
                          FOREIGN KEY (lesson_id) REFERENCES lessons (id)
                      );
                   """)
    conn.commit()

def get_db_conn(db_name: str):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn





