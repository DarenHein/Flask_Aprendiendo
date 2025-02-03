
from flask import Flask
from flask import jsonify
from main import producto 

app = Flask(__name__)

productos = producto()

@app.route('/')
def funcion():
	return jsonify(productos)

@app.route('/producto/<producto>')
def buscarProducto(producto):
	elemento = [x for x in productos if x["nombre"] == producto]
	if elemento : 
		return jsonify(elemento)
	else : 
		return "no encontramos nada "


if __name__ == '__main__' :
	app.run(debug=True)
