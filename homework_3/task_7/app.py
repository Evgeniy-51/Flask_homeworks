"""
Создайте форму регистрации пользователей в приложении Flask. Форма должна содержать поля: имя, фамилия, email, пароль
и подтверждение пароля. При отправке формы данные должны валидироваться на следующие условия:
    ○ Все поля обязательны для заполнения.
    ○ Поле email должно быть валидным email адресом.
    ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
    ○ Поле подтверждения пароля должно совпадать с полем пароля.
    ○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
    ○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.
"""

from flask import Flask, request, render_template, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from string import digits, ascii_letters

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
        surname = form.surname.data
        email = form.email.data
        password = form.password.data

        if valid_psw(password):
            password = generate_password_hash(password)
            new_user = User(name=name, surname=surname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Регистрация прошла успешно!")
        else:
            flash("Ошибка! Пароль должен содержать хотя бы одну букву и одну цифру!")

    return render_template("registration.html", form=form)


def valid_psw(psw):
    psw = set(psw)
    return bool(psw & set(ascii_letters)) and bool(psw & set(digits))


if __name__ == '__main__':
    app.run(debug=True)
