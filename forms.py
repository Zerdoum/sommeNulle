from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    #constant = StringField('Constant', validators=[DataRequired()])
    constant = SelectField('Constante', choices=[('0','D(G)'),('1','g(G)'),('2','s(G)'),('3','s_{≤k}(G)')], validators=[DataRequired()])
    #range = IntegerField('Range', validators=[DataRequired()])
    group = StringField('Le groupe abélien finis G:', validators=[DataRequired(),\
                                                                  Regexp('^[0-9,]*$', message="Merci de bien vouloir respecter la forme du groupe indiqué ci-dessous !!"),\
                                                                  Regexp('^.*\\d$', message="Le groupe doit terminer par un entier !!")])
    k = StringField('k', [Regexp('^[0-9]*$', message="k doit étre un entier !!")])
    submit = SubmitField('Calculer')

class SearchOneForm(FlaskForm):
    constant = ''
    value1 = IntegerField('Value', validators=[DataRequired()])
    submit = SubmitField('Search')
