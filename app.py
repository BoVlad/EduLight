from flask import *
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = "3D=79P\D+<SP9yU8;jGZ=z?u4Ow"

# @app.route('/')
# def index():
#     return render_template('/home')
