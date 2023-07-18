from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# модель таблицы автор
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'Authors({self.firstname}, {self.lastname})'


# модель таблицы книги
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    authors = db.relationship('Author', secondary='association', backref='books')

    # делает связь многие ко многим (указывается либо в одной моделе, либо в другой)

    def __repr__(self):
        return f'Books({self.title}, {self.year}, {self.count})'


# промежуточная таблица для связи многие ко многим
class Association(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
