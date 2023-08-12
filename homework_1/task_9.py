"""
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние
шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

main_menu = [
    {'name': 'Одежда', 'url': '/wear/'},
    {'name': 'Обувь', 'url': '/shoes/'},
]

wear_menu = [
    {'name': 'Куртки', 'url': '#'},
    {'name': 'Футболки', 'url': '#'},
    {'name': 'Свитера', 'url': '#'},
]

shoes_menu = [
    {'name': 'Туфли', 'url': '#'},
    {'name': 'Ботинки', 'url': '#'},
    {'name': 'Сапоги', 'url': '#'},
]


@app.route("/")
def index():
    return render_template("task_9_main.html", menu=main_menu)


@app.route("/wear/")
def wear():
    return render_template("task_9_wear.html", menu=wear_menu)


@app.route("/shoes/")
def shoes():
    return render_template("task_9_shoes.html", menu=shoes_menu)


if __name__ == '__main__':
    app.run(debug=True)
