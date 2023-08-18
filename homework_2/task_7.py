"""
Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        num = float(request.form.get("num"))
        return render_template("task7_res.html", num=num, res=num**2)

    return render_template("task7_form.html")


if __name__ == '__main__':
    app.run(debug=True)
