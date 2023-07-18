import random

from flask import Flask, render_template
from books_and_authors.models import db, Author, Book, Association

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_database.db'
db.init_app(app)


# инициализация БД
@app.cli.command('init-db_books')
def init_db():
    db.create_all()
    print('The database has been created')


# заполняем БД случайными данными
@app.cli.command('fill-db')
def fill_db():
    # заполнили БД случайными данными руками
    ...
    print(f'Books and authors added')


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная'
    }
    return render_template('index.html', **context)


# выводим все книги на страницу
@app.route('/books/')
def books():
    all_books = Book.query.all()

    context = {
        'title': 'Книги',
        'books': all_books
    }
    return render_template('books.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
