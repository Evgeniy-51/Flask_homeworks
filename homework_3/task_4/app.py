"""
Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
    ○ Имя пользователя (обязательное поле)
    ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
    ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
    ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite) и выводиться сообщение об
успешной регистрации. Если какое-то из обязательных полей не заполнено или данные не прошли валидацию, то должно
выводиться соответствующее сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в базе данных. Если такой
пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.
"""

from flask import Flask, request, render_template, flash
from flask_wtf.csrf import CSRFProtect
from models_db import db, User
from models_form import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dhgreghiw9ehgerhghtherthe"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.route("/", methods=["GET", "POST"])
@app.route("/reg/", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == "POST":
        if not form.validate():
            flash("Ошибка, неправильно заполнена форма!")
            return render_template("registration.html", form=form)

        name = form.name.data
        email = form.email.data
        password = form.password.data

        if is_unique(name, email):
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Регистрация прошла успешно!")
        else:
            flash("Ошибка! Такой пользователь уже существует!")

    return render_template("registration.html", form=form)


def is_unique(name, email):
    if User.query.filter(User.name == name).first():
        return False
    if User.query.filter(User.email == email).first():
        return False
    return True


if __name__ == '__main__':
    app.run(debug=True)
