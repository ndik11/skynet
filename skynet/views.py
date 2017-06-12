from wtforms import Form, TextField
from wtforms import validators

from skynet import app
from skynet.models import UserAdmin, PostAdmin, TreeView, User, db, Tag, Tree, lala, lolo
from skynet.skynet import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, Markup
import logging
import flask_admin as admin
from flask_admin.contrib import sqla


# Create admin
adminConsole = admin.Admin(app, name='Skynet: admin', template_mode='bootstrap3')
# Creating views
adminConsole.add_view(UserAdmin(User, db.session))
adminConsole.add_view(sqla.ModelView(Tag, db.session))
adminConsole.add_view(PostAdmin(db.session))
adminConsole.add_view(TreeView(Tree, db.session))
adminConsole.add_view(lala(lolo, db.session))


# @app.route('/')
# def show_entries():
#     db = get_db()
#     cur = db.execute('select title, text from entries order by id desc')
#     entries = cur.fetchall()
#     app.logger.debug('we are in the root')
#     return render_template('show_entries.html', entries=entries)


@app.route('/')
def root():
    xz = ('la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la', 'la')
    print(type(xz))
    title = 'root'
    username = 'Vasya Huev'
    app.logger.debug('we are in the root')
    return render_template('index.html', title = title, xz = xz, username = username)


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

    def reset(self):
        from werkzeug.datastructures import MultiDict
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)


@app.route("/hello", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error: All the form fields are required. ')

    return render_template('hello.html', form=form)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    app.logger.debug('new info added')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
            app.logger.debug('invalid uname')
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
            app.logger.debug('invalid pswd')
        else:
            session['logged_in'] = True
            flash('You were logged in')
            app.logger.debug('we are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    app.logger.debug('we are logged out')
    return redirect(url_for('show_entries'))


# Setup the logger
file_handler = logging.FileHandler('skynet/logs/apperror.log')
handler = logging.StreamHandler()
file_handler.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
app.logger.addHandler(handler)
app.logger.addHandler(file_handler)
