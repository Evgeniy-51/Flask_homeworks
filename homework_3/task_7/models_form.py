from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired("Введите имя!")])
    surname = StringField("Фамилия", validators=[DataRequired("Введите фамилию!")])
    email = StringField("Email", validators=[DataRequired("Введите E-mail!"), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Пароль должен быть не короче 8 символов!")])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password", "Пароли не совпадают!")])
    submit = SubmitField("Войти")