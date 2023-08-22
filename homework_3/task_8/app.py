"""
Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен
быть зашифрован.
"""

from flask import Flask, request, render_template, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash

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
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        new_user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Регистрация прошла успешно!")

    return render_template("registration.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
