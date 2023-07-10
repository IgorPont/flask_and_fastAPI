from flask import Flask, render_template

app = Flask(__name__)


# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
@app.route('/base/')
def base():
    return render_template('base.html')


@app.route('/about/')
def base_about():
    return render_template('base_about.html')


@app.route('/contacts/')
def base_contacts():
    return render_template('base_contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
