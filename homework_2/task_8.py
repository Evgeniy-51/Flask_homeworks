"""
Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить" При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет выведено "Привет, {имя}!".
"""
from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'iauhgphh5hy3vqhrgqhghh'


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form.get("name")
        flash(f"Привет, {name}!")
        return render_template("task8_res.html", name=name)
    return render_template("task8_form.html")


if __name__ == '__main__':
    app.run(debug=True)
