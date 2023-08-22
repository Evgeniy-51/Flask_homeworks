"""
Создать страницу, на которой будет форма для ввода имени и электронной почты. При отправке которой будет создан cookie
файл с данными пользователя Также будет произведено перенаправление на страницу приветствия, где будет отображаться
имя пользователя.
На странице приветствия должна быть кнопка "Выйти" При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("task9_home.html")


@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    name = request.form.get("name")
    email = request.form.get("email")
    response = make_response(redirect("/greet"))
    response.set_cookie("user_name", name)
    response.set_cookie("user_email", email)
    return response


@app.route('/greet')
def greet():
    user_name = request.cookies.get("user_name")
    if user_name:
        return render_template("task9_welcome.html", name=user_name)
    return redirect('/')


@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie("user_name")
    response.delete_cookie("user_email")
    return response


if __name__ == '__main__':
    app.run(debug=True)
