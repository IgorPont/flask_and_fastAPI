from flask import Flask, render_template

app = Flask(__name__)


# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!"
@app.route('/')
def hello_world():
    return f'Hello World!'


# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".
@app.route('/about/')
def about():
    return f'<h1>About</h1>'


@app.route('/contacts/')
def contacts():
    return f'<h1>Contacts</h1>'


# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.
@app.route('/sum/<int:num1>/<int:num2>/')
def sum(num1: int, num2: int):
    return f'{num1 + num2}'


# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.
@app.route('/text/<text>/')
def get_len(text: str):
    return f'{len(text) = }'


# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".
@app.route('/html/')
def get_html():
    return render_template('index.html')


# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
@app.route('/students/')
def students():
    students = [{'first_name': 'Ivan1', 'last_name': 'Ivanov1', 'age': '20', 'score': '5'},
                {'first_name': 'Ivan2', 'last_name': 'Ivanov2', 'age': '21', 'score': '4'},
                {'first_name': 'Ivan3', 'last_name': 'Ivanov3', 'age': '22', 'score': '3'},
                {'first_name': 'Ivan4', 'last_name': 'Ivanov4', 'age': '23', 'score': '2'},
                {'first_name': 'Ivan5', 'last_name': 'Ivanov5', 'age': '24', 'score': '1'}]
    return render_template('students.html', students=students)


# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
@app.route('/news/')
def news():
    news = [{'title': 'News1', 'text': 'Text1', 'date': '20.06.2023'},
            {'title': 'News2', 'text': 'Text2', 'date': '21.06.2023'},
            {'title': 'News3', 'text': 'Text3', 'date': '22.06.2023'},
            {'title': 'News4', 'text': 'Text4', 'date': '23.06.2023'}]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)
