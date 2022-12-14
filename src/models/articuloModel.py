from models.model import Model
from pymysql.cursors import DictCursor
import os

class ArticuloModel(Model):
    def __init__(self, app):
        super().__init__(app)
        app.config['MYSQL_DATABASE_DB'] = 'empleados'
        app.config['UPLOADS'] = os.path.join('src/uploads')
        self.__uploads = app.config['UPLOADS']
        self.__connection = self.DB.connect();
        self.__cursor = self.__connection.cursor(cursor=DictCursor)

    def getAll(self):
        self.__cursor.execute("SELECT * FROM empleado;")
        registro = self.__cursor.fetchall()
        self.__connection.commit()
        return registro
    
    def getByID(self, id):
        self.__cursor.execute("SELECT * FROM empleado WHERE id = (%s);", [id])
        registro = self.__cursor.fetchone()
        self.__connection.commit()
        return registro

    def postEmpleado(self, nombre, correo, nombreFoto="empty"):
        datos = (nombre, correo, nombreFoto)
        self.__cursor.execute("INSERT INTO empleado (nombre, correo, foto) values (%s, %s, %s);", datos)
        return self.__connection.commit()

    def update(self, nombre, correo, nombreFoto, id):
        datos = (nombre, correo, nombreFoto, id)
        self.__cursor.execute("UPDATE empleado SET nombre=(%s), correo=(%s), foto=(%s) WHERE id=(%s)", datos)
        return self.__connection.commit()

    def delete(self, id):
        self.__cursor.execute("SELECT foto FROM empleado WHERE id = (%s)", [id])
        nombreFoto = self.__cursor.fetchall()
        self.__connection.commit()
        try:
            os.remove(os.path.join(self.__uploads, nombreFoto[0]))
        except:
            pass
        self.__cursor.execute("DELETE FROM empleado WHERE id = (%s)", [id])
    
    def getFotoByID(self, id):
        self.__cursor.execute("SELECT foto FROM empleado WHERE id=%s", [id])
        registro = self.__cursor.fetchone()
        self.__connection.commit()
        return registro

    @property
    def connection(self):
        return self.__connection

    