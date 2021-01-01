from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    remember_me = BooleanField('Remember Me')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    remember_me = BooleanField('Remember Me')

class EditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    stock = StringField('Favorite Stock')
    state = StringField('Home State')
    age = IntegerField('Age')
    dob = DateField('Date of Birth', format='%Y-%m-%d')
    submit = SubmitField('Save')
