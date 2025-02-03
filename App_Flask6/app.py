

# todo vamos a jugar con el update en flask 

from flask import Flask 
from flask import jsonify , request
from recursos import * 

app = Flask(__name__)

@app.route('/')
def raiz():
    return "hola mundo"

@app.route('/agregar',methods=['POST'])
def agregar():

    data = request.json

    if not data : 
        return "falta de datos"
    else : 
        
        Serializacion(data)
        return "datos recibidos"
    


if __name__ == "__main__": 
    app.run(debug=True,port=4000)