
# retorno de una sola imgen de un servidor de python 

from flask import Flask ,send_from_directory
from flask import jsonify 

app = Flask(__name__)

# vamos a apliacar los metodos get post put y delete en  flask 

# metodo get 
@app.route('/' , methods=['GET'])
def rutaget():
	return "Hola mundo"
# devolveremos un archivo multimedia jpg desde una 

# retornar una imagen 
@app.route('/File/<filename>',methods=['GET'])
def ruta_imagenes(filename):
	return send_from_directory('static',filename)

if __name__ == '__main__': 
	app.run(debug=True)
