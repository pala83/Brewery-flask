from flask import render_template
from models.articuloModel import ArticuloModel
from models.cervezaModel import CervezaModel

class Controller:
    def __init__(self, app):
        self.articuloModel = ArticuloModel(app)
        self.cervezaModel = CervezaModel(app)
        self.__nav = {
            "home":False,
            "catalogo":False,
            "comprar":False,
            "admin":False
        }

    def showHome(self):
        posicion = self.__nav.copy()
        posicion["home"]=True
        return render_template('views/index.html', activados=posicion)

    def showCatalogo(self):
        posicion = self.__nav.copy()
        posicion["catalogo"]=True
        cervezas = self.cervezaModel.getAll()
        return render_template('views/catalogo.html', activados=posicion, cervezas=cervezas)
    
    def showCompras(self):
        posicion = self.__nav.copy()
        posicion["comprar"]=True
        return render_template('views/compras.html', activados=posicion)

    def showAdmin(self):
        posicion = self.__nav.copy()
        posicion["admin"]=True
        return render_template('views/admin.html', activados=posicion)

    def showLogin(self):
        return render_template('views/login.html', activados=self.__nav)

    def showSignIn(self):
        return render_template('views/registro.html', activados=self.__nav)