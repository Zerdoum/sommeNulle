# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, flash, redirect,request
from forms import RegistrationForm, LoginForm, SearchForm, SearchOneForm
from core import getConstant


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eivai9rie4aepai9eele6Iedaec6siew'

posts = [
    {
        'title': 'DavenPort',
        'content': 'First post content',
    },
    {
        'title': 'Harborth',
        'content': 'Second post content',
    },
    {
        'title': 'Erdos-Ginzburgviv',
        'content': 'Second post content',
    },
    {
        'title': 'Olson',
        'content': 'Second post content',
    },
    {
        'title': 'Others',
        'content': 'Second post content',
    }

]

@app.route("/")
@app.route("/home")
def home():
    form = SearchForm()
    return render_template('home.html', posts=posts, form=form)

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
@app.route("/search/<constant>/<group>", methods=('GET','POST'))
@app.route("/search/<constant>/<group>/<result>", methods=('GET','POST'))
def search(constant='', range='', group='', result=''):
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('searchOne', constant=form.constant.data, group=form.group.data))
    return render_template('search.html', title='Search', form=form, constant=constant, group=group, result=result)

@app.route('/searchOne/<constant>/<group>')
def searchOne(constant, group):
    form = SearchOneForm()
    listValues = group.split(",")
    result = getConstant(constant, listValues)
    return redirect(url_for('search', constant=constant, group=group, result=result))

@app.route("/description", methods=('GET', 'POST'))
def description():
    form = SearchForm()
    type = request.args.get('type')
    return render_template('description.html', title='Description', form=form, type=type)