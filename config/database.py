
HOST='localhost'
PORT=3306
USERNAME='root'
PASSWORD='123456'
DATABASE= 'elishop'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 60
SQLALCHEMY_POOL_RECYCLE = 10
SQLALCHEMY_MAX_OVERFLOW = 5
SQLALCHEMY_TRACK_MODIFICATIONS = False