import random

from flask import Flask, render_template
from student_record.models import db, Faculty, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_database.db'
db.init_app(app)


# инициализация БД
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('The database has been created')


# заполняем БД случайными данными
@app.cli.command('fill-db')
def fill_db():
    count = 5

    # добавляем факультеты
    for j in range(1, count + 1):
        new_faculty = Faculty(name=f'Faculty{j}')
        db.session.add(new_faculty)

    # добавляем студентов
    for i in range(1, count * 2 + 1):
        new_student = Student(
            firstname=f'Name{i}',
            lastname=f'Lastname{i}',
            age=random.randint(18, 55),
            gender=random.choice(['male', 'female']),
            group=i % count + 1,
            faculty_id=i % count + 1,
        )
        db.session.add(new_student)

    db.session.commit()
    print(f'Students and faculties added')


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная'
    }
    return render_template('index.html', **context)


# выводим всех студентов на страницу
@app.route('/students/')
def students():
    all_students = Student.query.all()

    context = {
        'title': 'Студенты',
        'students': all_students
    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
