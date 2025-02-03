from flask import Flask 
from flask import jsonify,request
from recursos import *
# todo vamos a mandar desde thunder client un json a una ruta post en el server 

app = Flask(__name__)

lista = recursos2()

# todo ruta de prueba 
@app.route('/')
def ruta_principal():
    return jsonify(lista)

#todo ruta post que recibe un aprametro 
@app.route('/recibiendo', methods=['POST'])
def recibiendo():
    print(request.json) # todo elemento que llega 
    # todo vamos a agregarlos al que ya tenemos 
    lista.append(request.json) #todo elemento agregando ala lista de nuevos elementos 
    for elementos in lista : 
        print(elementos) # mostramos todos los elementos que tenemos hasta el momento 
    # todo ahora agregaremos el contenido a un archivo json 
    serializacion(lista)
    return "recibido"

# todo ahora vamos a acutalizar el nombre de una propiedad del json ya creado 
@app.route('/actualizar',methods=['PUT'])
def actualizar():
    # todo primero leemos el json pero esto lo aremos en el documetno recursos 
    new_list = deserilizacion()
    print(new_list)
    # todo ya leemos los datos del json ahora hay que actualizar uno 
    print(request.json) # todo llega el nuevo dato 
    filtrado = [x for x in new_list if x["name"] == request.json["name"]]
    print("nombre filtrado : ",filtrado)
    if filtrado : 
        print("existe el nomrbe de la persona en new list")
        filtrado["name"] = request.json["new_name"]
        print(filtrado)
        serializacion(filtrado)
    else :
        print("no existe el nombre ingresado en new list")
    return jsonify(new_list)



if __name__ == '__main__':
    app.run(debug=True,port=4000)