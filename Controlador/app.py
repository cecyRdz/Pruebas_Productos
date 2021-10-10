from flask import Flask,render_template,request
app = Flask(__name__, template_folder='../vista')

@app.route('/')
def inicio():
    return render_template('comunes/Principal.html')

@app.route('/consultarProductos')
def consultarProductos():
    return render_template('Productos/consultarProductos.html')

@app.route('/registrarProducto')
def registrarProducto():
    return render_template('Productos/registrarProducto.html')

@app.route('/registrarNuevoProducto',methods=['post'])
def registrarNuevoProducto():
    nombre = request.form['nombre']
    return 'Se guardaron los cambios del producto: '+nombre

@app.route('/ModificarProducto')
def ModificarProducto():
    return render_template('Productos/editarProducto.html')

@app.route('/recopilarDatosEditados',methods=['post'])
def recopilarDatosEditados():
    idProducto = request.form['idProducto']
    return 'Se guardaron los cambios del producto: '+idProducto

@app.route('/EliminarProducto')
def EliminarProducto():
    return render_template('Productos//EliminarProducto.html')

if __name__ == '__main__':
    app.run(debug=True)
