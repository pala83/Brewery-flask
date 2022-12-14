from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from datetime import datetime
from models.articuloModel import ArticuloModel
from controllers.controller import Controller
import os

app = Flask(__name__)
modelArtc = ArticuloModel(app)
controller = Controller(app)
nav = {
    "home":False,
    "catalogo":False,
    "comprar":False,
    "admin":False
}

@app.route('/fotobirra/<path:nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(os.path.join('uploads'), nombreFoto)

@app.route('/')
def home():
    return controller.showHome()

@app.route("/login")
def login():
    return controller.showLogin()

@app.route("/registro")
def registro():
    return controller.showSignIn()

@app.route('/catalogo')
def catalogo():
    return controller.showCatalogo()

@app.route('/comprar')
def comprar():
    return controller.showCompras()

@app.route('/admin')
def admin():
    return controller.showAdmin()

@app.route('/empleados')
def form_empleado():
    return render_template('empleados/create.html')

@app.route('/empleados/crear', methods=["POST"])
def alta_empleado():        
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    if _nombre == '' or _correo == '':
        flash('El nombre y el correo son obligatorios.')
        return redirect(url_for('form_empleado'))
    if _foto.filename != '':
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreFoto = tiempo + '_' + _foto.filename
        _foto.save("src/uploads/" + nuevoNombreFoto)
    modelArtc.postEmpleado(_nombre, _correo, nuevoNombreFoto)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    modelArtc.delete(id)
    return redirect('/')

@app.route('/modify/<int:id>')
def modify(id):
    empleado = modelArtc.getByID(id)
    return render_template('empleados/edit.html', empleado=empleado)

@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    id = request.form['txtId']

    # datos = (_nombre, _correo, id)

    if _foto.filename != '':
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreFoto = tiempo + '_' + _foto.filename
        _foto.save("src/uploads/" + nuevoNombreFoto)
    modelArtc.update(_nombre, _correo, nuevoNombreFoto, id)
    nombreFoto = modelArtc.getFotoByID(id)
    try:
        os.remove(os.path.join(app.config['UPLOADS'], nombreFoto))
    except:
        pass
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
