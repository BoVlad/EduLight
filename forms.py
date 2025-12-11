from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

import email_validator


class LoginForm(FlaskForm):
    email = StringField("Електронна пошта", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Увійти")

class RegisterForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired(), Length(min=4, max=24)])
    email = StringField("Електронна пошта", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Зареєструватися")