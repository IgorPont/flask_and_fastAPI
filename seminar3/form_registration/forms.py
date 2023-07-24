from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


# форма регистрации
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def validate_password(self, field):
        if not any(map(str.isdigit, field.data)):
            raise ValidationError('Пароль должен содержать хотя бы одну цифру')
        if not any(map(str.isalpha, field.data)):
            raise ValidationError('Пароль должен содержать хотя бы одну букву')
