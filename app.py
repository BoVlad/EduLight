from flask import *
import sqlite3
from DB_utilts import all_db_start, get_db_conn

app = Flask(__name__)
app.config['SECRET_KEY'] = "3D=79PaD+<SP9yU8;jGZ=z?u4Ow"

all_db_start()


@app.get("/")
def index():
    # return render_template('/home')
    pass



@app.get("/login")
def get_login():
    return render_template("login.html")

@app.post("/login")
def post_login():
    action = request.form.get("action")
    if action == "login":
        username = request.form.get("username")
        password = request.form.get("password")
