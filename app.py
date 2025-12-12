import sqlite3
import bcrypt
import random

from flask import *
from DB_utilts import all_db_start, get_db_conn, check_user_in_db, add_user_to_db, get_search_from_db
from datetime import timedelta
from forms import LoginForm, RegisterForm
from session_utilts import login_required, login_forbidden, user_in_session

app = Flask(__name__)
app.config['SECRET_KEY'] = "3D=79PaD+<SP9yU8;jGZ=z?u4Ow"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=2)

all_db_start()


@app.get("/")
def index():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    data = cursor.fetchall()
    courses_quantity = min(4, len(data))
    courses = random.sample(data, k=courses_quantity)
    conn.close()
    return render_template("index.html", courses=courses, user_logined=user_in_session())

@app.get("/search")
def search():
    q = request.args.get("q", default="", type=str)
    return {
        "q": q,
        "len": len(q),
    }



@app.get("/profile")
@login_required
def get_profile():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE email = ?", (session["user_email"],))
    username = cursor.fetchone()[0]
    conn.close()
    return render_template("profile.html", username=username)

@app.post("/profile")
@login_required
def post_profile():
    session["user_email"] = None
    return redirect(url_for("index"))



@app.get("/about")
def about():
    return render_template("about.html", user_logined=user_in_session())


@app.get("/register")
@login_forbidden
def get_register():
    form = RegisterForm()
    return render_template("register.html", form=form)

@app.post("/register")
@login_forbidden
def post_register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email_form = form.email.data
        password_form = form.password.data
        check_user = check_user_in_db(email_form, password_form)
        if check_user is None:
            add_user_to_db(username, email_form, password_form)
            session["user_email"] = email_form
            return redirect(url_for("index"))
        if check_user:
            error = "Такий користувач вже існує!"
            return render_template('register.html', form=form, error=error)
    return render_template('register.html', form=form)

@app.get("/login")
@login_forbidden
def get_login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.post("/login") #TODO не работает логин с testuser!
@login_forbidden
def post_login():
    form = LoginForm()
    if form.validate_on_submit():
        email_form = form.email.data
        password_form = form.password.data
        check_user = check_user_in_db(email_form, password_form)
        if check_user:
            session["user_email"] = email_form
            return redirect(url_for("index"))
        if check_user is None or not check_user:
            error = "Неправильна пошта або пароль"
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True, port=2738)