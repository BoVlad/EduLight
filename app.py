import sqlite3
import bcrypt

from flask import *
from functools import wraps
from DB_utilts import all_db_start, get_db_conn, check_user_in_db
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = "3D=79PaD+<SP9yU8;jGZ=z?u4Ow"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=2)

all_db_start()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))  # перекидываем на главную
        return f(*args, **kwargs)
    return decorated_function




@app.get("/")
def index():
    return render_template("index.html")

@app.get("/register")
def get_register():
    return render_template("register.html")





@app.get("/login")
def get_login():
    return render_template("login.html")

@app.post("/login")
def post_login():
    action = request.form.get("action")
    if action == "login":
        username_form = request.form.get("username")
        password_form = request.form.get("password")
        if check_user_in_db(username_form, password_form):
            session["user_id"] = username_form
            return redirect(url_for("index"))
        else:
            flash("Користувача з таким іменем немає, або пароль введено невірно!")
    elif action == "register":
        return redirect(url_for("get_register"))
    return None




if __name__ == '__main__':
    app.run(debug=True, port=2738)