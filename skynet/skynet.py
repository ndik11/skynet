try:
    import os
    import config
    from flask import Flask, request, session, g, redirect, url_for, abort, \
         render_template, flash
    from flask_sqlalchemy import SQLAlchemy
except ImportError as err:
    raise err


app = Flask(__name__)
app.config.from_object('config.TestingConfig')
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello world!'


app.run()
