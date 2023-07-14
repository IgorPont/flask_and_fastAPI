from pathlib import PurePath, Path
from flask import Flask, request, render_template, abort, flash, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


# выводим страницу с кнопкой
@app.route('/')
def main():
    return render_template('index.html')


# после нажатия на кнопку редиректим на страницу с приветствием
@app.route('/hello/')
def hello():
    return f'Привет'


# загружаем файл на сервер через страницу (должна быть создана папка, куда будут загружаться файлы, в данном случае
# "uploads")
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('index.html')


# работаем с логином и паролем
users = {
    'user1': 'password1',
    'user2': 'password2'
}


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login not in users or users.get(login) != password:
            return f'Неверно введен логин или пароль'
        else:
            return f'Рад видеть тебя, {login}!'
    return render_template('index.html')


# забираем введенный текст на странице и обрабатываем его
@app.route('/text_input/', methods=['GET', 'POST'])
def text_input():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Количество слов в введенном тексте равно {len(text.split())}'
    return render_template('index.html')


# делаем калькулятор (принимаем операции и цисла, выводим результат)
@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        operation = request.form.get('operation')
        match operation:
            case 'add':
                return f'{num1 + num2}'
            case 'subtract':
                return f'{num1 - num2}'
            case 'multiply':
                return f'{num1 * num2}'
            case 'divide':
                return f'{num1 / num2}' if num2 != 0 else 'ZeroDivisionError: division by zero'
    return render_template('index.html')


# проверям возраст и выводим ошибку, если не соответствует
@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('num'))
        if age < 18:
            abort(403)
        return f'Привет, {name}! Ты подходишь!'
    return render_template('index.html')


# выводим ошибку проверки возраста
@app.errorhandler(403)
def error403(e):
    return render_template('error403.html'), 403


# Выводим flash-сообщения над полем формы

# генерируем секретный ключ
# >>> import secrets
# >>> secrets.token_hex()
app.secret_key = '6ff5a3dbd5c3f5985d4b05da494e45179a8f27a6fc938593a811184debdc3e0c'


@app.route('/flash_name/', methods=['GET', 'POST'])
def flash_name():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('flash_name'))
        flash('Форма успешно отправлена', 'success')
        return redirect(url_for('flash_name'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
