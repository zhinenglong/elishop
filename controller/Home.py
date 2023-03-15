import app
from app import dba
from .Controller import Controller
from models.User import User
from sqlalchemy import func
from tasks.tasks import echodoc

class Home(Controller):

    def home(cls):

        users = dba.session.execute(dba.select(User)).scalars()

        print(users.one().name)
        echodoc.apply_async()

        return cls.render("home/home.html", name="eeee", body="hellow")
