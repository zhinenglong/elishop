from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = None
dba = None
def makeApp() -> Flask:
    return Flask(__name__, template_folder='views')

def makeDba() -> SQLAlchemy:
    return SQLAlchemy()

if app is None:
    app = makeApp()
    app.config.update(DEBUG=True)
    database_dir = 'config/database.py'
    if os.path.exists(app.root_path +'/'+ database_dir):
        app.config.from_pyfile(database_dir)
    if dba is None:
        dba = makeDba()
        dba.init_app(app)
else:
    if dba is None:
        dba = makeDba()
        dba.init_app(app)



