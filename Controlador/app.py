from flask import Flask,render_template
app = Flask(__name__, template_folder='../vista')

@app.route('/')
def inicio():
    return render_template('comunes/Principal.html')

@app.route('/consultarProductos')
def consultarProductos():
    return render_template('Productos/consultar.html')

if __name__ == '__main__':
    app.run(debug=True)
