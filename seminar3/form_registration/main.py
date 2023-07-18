from flask import Flask, request, render_template, abort, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from form_registration.models import db, User
from form_registration.forms import RegistrationForm

# работа с формами (обязательно защищаем от CSRF-атак, создаем ключ)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_database.db'
db.init_app(app)


# инициализация БД
@app.cli.command('init-db_users')
def init_db():
    db.create_all()
    print('The database has been created')


# заполняем БД случайными данными
@app.cli.command('fill-db')
def fill_db():
    ...
    print(f'The database is full')


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная'
    }
    return render_template('index.html', **context)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

        new_user = User(
            username=username,
            email=email,
            # хешируем пароль
            password=generate_password_hash('password'),
        )
        db.session.add(new_user)
        db.session.commit()

    return render_template('registration.html', form=form)


# приветствуем зарегистрированного пользователя
@app.route('/greeting/')
def greeting():
    return render_template('greeting.html')


# выводим всех юзеров из БД
@app.route('/users/')
def users():
    users = User.query.all()
    res = ", ".join([user.username for user in users])
    return res


if __name__ == '__main__':
    app.run(debug=True)
