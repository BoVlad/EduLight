from functools import wraps
from flask import session, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_email") is None:
            return redirect(url_for("get_login"))
        return f(*args, **kwargs)
    return decorated_function


def login_forbidden(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_email") is not None:
            return redirect(url_for("get_login"))
        return f(*args, **kwargs)
    return decorated_function


def user_in_session():
    return session.get("user_email") is not None