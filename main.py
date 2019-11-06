from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, SearchForm, SearchOneForm
from core import getConstant

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eivai9rie4aepai9eele6Iedaec6siew'

posts = [
    {
        'author': 'Hanane Zerdoum',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '01 Nouvembre 2019'
    },
    {
        'author': 'Hanane Zerdoum',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '01 Nouvembre 2019'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'sucess')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and passwrod !', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/search", methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
            return redirect(url_for('searchOne', constant=form.constant.data, range=form.range.data, group=form.group.data ))
    return render_template('search.html', title='Search', form=form)

@app.route('/searchOne/<constant>/<range>/<group>')
def searchOne(constant, range, group):
    form = SearchOneForm()
    listValues = group.split(",")
    result = getConstant(constant, range, listValues)
    return render_template('searchOne.html', title='Search_one', result=result)
