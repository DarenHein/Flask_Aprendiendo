from flask import Flask 

app = Flask(__name__)

@app.route('/home')
def home():
	return '<h1 style="color: red;">Me la Pela Axel</h1>'

@app.route('/baño')
def baño():
	return "hola desde el endpoint baño"

@app.route('/')
def raiz():
	return "ruta raiz de mi servidor"

app.run(debug=True, port=5000)
