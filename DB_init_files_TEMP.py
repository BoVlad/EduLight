import sqlite3
import bcrypt

def db_init_courses_temp():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    courses = [("C++ для початківців",
         "Вивчіть C++ з нуля до професійного рівня через практичні приклади та проекти.",
         "Цей курс допоможе вам освоїти мову програмування C++ з нуля.\n\n"
         "Ви пройдете всі ключові теми — від базових типів даних, умовних операторів та циклів до об’єктно-орієнтованого програмування та роботи з файлами.\n"
         "Курс включає практичні завдання та проекти, що дозволить закріпити знання та підготуватися до роботи програмістом.\n"
         "Після завершення курсу ви зможете створювати власні програми, працювати з алгоритмами та структурами даних, а також застосовувати C++ у реальних проектах.",
         "static/images/C++.png", 12),

        ("Web-розробка (HTML, CSS, JS) для початківців",
         "Освойте фронтенд веб-розробку з нуля через практичні приклади та проекти.",
         "Цей курс допоможе вам створювати сучасні веб-сайти з нуля.\n\n"
         "Ви навчитеся основам HTML, CSS та JavaScript, створювати адаптивні макети, інтерактивні елементи та анімації.\n"
         "Курс включає практичні завдання та проекти, що дозволить одразу застосовувати знання на практиці.\n"
         "Після завершення курсу ви зможете створювати повноцінні веб-сайти та інтерактивні веб-додатки.",
         "static/images/WEB.png", 12),

        ("Java для початківців",
         "Вивчіть Java з нуля до професійного рівня через практичні приклади та проекти.",
         "Цей курс допоможе вам освоїти мову програмування Java з нуля.\n\n"
         "Ви пройдете всі ключові теми — від базових типів даних, умовних операторів та циклів до об’єктно-орієнтованого програмування, колекцій та роботи з файлами.\n"
         "Курс включає практичні завдання та проекти, що дозволить закріпити знання та підготуватися до роботи програмістом.\n"
         "Після завершення курсу ви зможете створювати власні програми, працювати з алгоритмами та структурами даних, а також застосовувати Java у реальних проектах.",
         "static/images/Java.png", 12),

        ("C# для початківців",
         "Вивчіть C# з нуля до професійного рівня через практичні приклади та проекти.",
         "Цей курс допоможе вам освоїти мову програмування C# з нуля.\n\n"
         "Ви пройдете всі ключові теми — від базових типів даних, умовних операторів та циклів до об’єктно-орієнтованого програмування та створення графічних додатків.\n"
         "Курс включає практичні завдання та проекти, що дозволить закріпити знання та підготуватися до роботи програмістом.\n"
         "Після завершення курсу ви зможете створювати власні програми, працювати з Windows Forms, WPF та іншими технологіями C# у реальних проектах.",
         "static/images/Csharp.png", 12),
    ]

    cursor.executemany("""
                       INSERT INTO courses (title, description_short, description, img, modules_quantity)
                       VALUES (?, ?, ?, ?, ?)
                       """, courses)
    conn.commit()
    conn.close()


def db_init_user_admin():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    salt = bcrypt.gensalt()
    password_input_hashed = bcrypt.hashpw("AdminOnDebug".encode('utf-8'), salt)

    cursor.execute("""INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)""",
                   ('Admin', 'admin@gmail.com', password_input_hashed))
    conn.commit()
    conn.close()

def update_course():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE courses SET title = ? WHERE id = ?",
        ("Python для початківців", 1)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET title = ? WHERE id = ?",
        ("C++ для початківців", 2)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET title = ? WHERE id = ?",
        ("WEB (HTML + CSS + JS) для початківців", 3)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET title = ? WHERE id = ?",
        ("Java для початківців", 4)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET title = ? WHERE id = ?",
        ("Csharp для початківців", 5)
    )
    conn.commit()



    cursor.execute(
        "UPDATE courses SET img = ? WHERE id = ?",
        ("Python.png", 1)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET img = ? WHERE id = ?",
        ("C++.png", 2)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET img = ? WHERE id = ?",
        ("WEB.png", 3)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET img = ? WHERE id = ?",
        ("Java.png", 4)
    )
    conn.commit()
    cursor.execute(
        "UPDATE courses SET img = ? WHERE id = ?",
        ("Csharp.png", 5)
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_course()