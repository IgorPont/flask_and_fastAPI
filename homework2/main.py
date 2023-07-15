from pathlib import PurePath, Path
from flask import Flask, request, render_template, abort, flash, redirect, url_for, session
from werkzeug.utils import secure_filename

app = Flask(__name__)

"""
Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить".
При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное число и 
его квадрат.
"""


@app.route('/', methods=['GET', 'POST'])
def square_number():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return f'{num}^2 = {num ** 2}'
    return render_template('index.html')


"""
Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан 
cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет 
отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными 
пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""

app.secret_key = '6ff5a3dbd5c3f5985d4b05da494e45179a8f27a6fc938593a811184debdc3e0c'


@app.route('/private_office')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('private_office.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        session['email'] = request.form.get('email') or 'NoEmail'
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
