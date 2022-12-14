from flaskext.mysql import MySQL
from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, app):
        self.__mysql = MySQL()
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
        app.config['SECRET_KEY'] = 'codoacodo'
        self.__mysql.init_app(app)
    
    @property
    def DB(self):
        return self.__mysql

    @abstractmethod
    def getAll(self):
        pass
"""
    @abstractmethod
    def getByID(self):
        pass
"""