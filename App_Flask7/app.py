from flask import Flask, render_template , send_file
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


# todo parametros opcionales 
@app.route("/opcional")
@app.route('/opcional/<nombre>')
def opcional(nombre = "opcional"):
    return f" hola {nombre}"

#todo parametros con tipo int 
@app.route("/numeros/<int:a>/<int:b>")
def ruta_numero(a,b):
    resultado = a + b 
    return resultado


'''
hemos estado regresando texto 
json , html 
ahora regresaremos una imagen desde el server o archivo crudo 

ocuapando send file 
'''

@app.route('/imagen')
def descarga_imagen():
    ruta = "wallhaven-p9g57m.png"
    return send_file(ruta)#as_attachment=True para que inicie la descarga 
    # si dolo dejamos senf_file solo la muestra en el navegador 

# todo cunado una ruta no o endponti no se encutra en el servidor 
# hay que mandarlo a un cath-all 
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "Lo siento la pagina no existe vuvleve a intentarlo "

if __name__  == "__main__":
    app.run(debug=True)