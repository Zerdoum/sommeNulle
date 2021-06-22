# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, flash, redirect,request
from forms import RegistrationForm, LoginForm, SearchForm, SearchOneForm
from core import getConstant


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eivai9rie4aepai9eele6Iedaec6siew'

posts = [
    {
        'title': 'DavenPort  D(G)',
        'content': 'DavenPort',
    },
    {
        'title': 'Harborth  g(G)',
        'content': 'Harborth',
    },
    {
        'title': 'Erdös-Ginzburg-Ziv  s(G)',
        'content': 'Erdös-Ginzburg-Ziv',
    },
    {
        'title': 'Généralisation de la constante d\'Erdös-Ginzburg-Ziv  s_{≤k}(G)',
        'content': 'Erdös-Ginzburg-Ziv inf',
    },

]

@app.route("/")
@app.route("/home")
def home():
    form = SearchForm()
    return render_template('home.html', posts=posts, form=form)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/search", methods=('GET', 'POST'))
@app.route("/search/<constant>/<group>/<result>", methods=('GET','POST'))
def search(constant='', range='', group='', result=''):
    form = SearchForm()
    if form.validate_on_submit():
        constant = form.constant.data
        group = form.group.data
        k = form.k.data
        listValues = group.split(",")
        result = getConstant(constant, listValues,k)
    return render_template('search.html', title='Search', form=form, constant=constant, group=group, result=result)

@app.route("/description", methods=('GET', 'POST'))
def description():
    form = SearchForm()
    type = request.args.get('type')
    return render_template('description.html', title='Description', form=form, type=type)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=False)