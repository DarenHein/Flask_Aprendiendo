# importaciones 
from flask import Flask 
from flask import jsonify # mandamos respuestas en formato json 

#creamos la aplicaion flask 
app = Flask(__name__)


# creacion de la ruta basica con flask 
@app.route('/',methods=['GET'])

# creamos funcion que se toma como ruta 
def home():
	return jsonify({
	     "mensaje" : "hola desde flask",
	     "status" : "Exitoso"
	}) 

# ahora el metodo que correra el server 

if __name__ == '__main__':
	app.run(debug=True)


