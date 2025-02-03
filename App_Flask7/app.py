from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# todo vamos a hacr un estudiada basica de flask 
#! creacion de tutas basica 
@app.route("/")
def raiz():
    return "Hola mundo",200 # con este numeor mandamos el estado de la consulta 

# ! vamos a mandar un nombre por medio de la url y la app lo va alamcenar 
@app.route("/nombre/<nombre>")
def ruta_name(nombre):
    return f"hola {nombre}" , 200

#! ahora ocuapremos un json que enviaremos desde aqui ala cliente  
diccionario = {
    "nombre" : "Luis",
    "edad" : 30 ,
    "Sexo" : "masculino"
}
@app.route("/persona")
def ruta_personas():
    return jsonify(diccionario)

#! ahora mandaaremos un html desde una ruta 
# todo tiene que existir una carpeta llamada template 
@app.route("/plantilla")
def plantilla():
    return render_template("index.html")


if __name__  == "__main__":
    app.run(debug=True)