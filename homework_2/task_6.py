"""
Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form.get("name")
        age = int(request.form.get("age"))
        if age in range(18, 110):
            return render_template("task6_res.html", name=name, age=age)
        else: return render_template("task6_err.html")

    return render_template("task6_form.html")


if __name__ == '__main__':
    app.run(debug=True)
