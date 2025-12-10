import sqlite3
import bcrypt
import random

from flask import *
from functools import wraps
from DB_utilts import all_db_start, get_db_conn, check_user_in_db
from datetime import timedelta
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "3D=79PaD+<SP9yU8;jGZ=z?u4Ow"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=2)

all_db_start()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_email" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function

def login_forbidden(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_email" in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function


def user_in_session():
    if session.get("user_email") is None:
        return False
    else:
        return True


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



@app.get("/register")
def get_register():
    return render_template("register.html")


@app.get("/login")
@login_forbidden
def get_login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.post("/login")
@login_forbidden
def post_login():
    form = LoginForm()
    if form.validate_on_submit():
        email_form = form.email.data
        password_form = form.password.data
        if check_user_in_db(email_form, password_form):
            session["user_email"] = email_form
            return redirect(url_for("index"))
    return render_template('index.html', form=form)




if __name__ == '__main__':
    app.run(debug=True, port=2738)