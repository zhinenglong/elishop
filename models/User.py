from . import dba

class User(dba.Model):
    __tablename__ = 'user'
    id = dba.Column(dba.Integer, primary_key=True)
    name = dba.Column(dba.String(100),nullable= False )
