
#todo objeto request 

from flask import Flask , request , make_response , redirect 

app = Flask(__name__)

@app.route('/')
def home():
    return "hola mundo "

#objeto request 

@app.route('/home_ip')
def home_ip():
    ip_host = request.remote_addr
    return f"{ip_host}"


#todo creacion de cookies 
# las cokiees son archivosque guardan inromacion en nuestro navegadro 
'''
crearemos una ruta que redireccione a otra ruta y a su ves un cookie que almacene la
ip de nuestro cleinte 
'''

@app.route('/ruta')
def ruta():
    ip = request.remote_addr # tomamos la ip del usuario 
    response = make_response(redirect('/ruta_redireccion')) # alamcena la redireccion en una variable 
    response.set_cookie("direccion ip" , ip) # crea una cokkie con la ip del usuario 
    return response  # response con la redireccion 

#todo ruta 
@app.route('/ruta_redireccion')
def ruta2():
    #ahora tomamosla cokkie 
    ip = request.cookies.get("direccion ip") # todo tomamos la cookie que se a almacenado en el navegador vendria siendo direccion ip como una llave para acceder al dato 
    '''
        direccion ip : ip # esta contiene la direccion ip o el dato 
        recojido de la otra ruta 
    '''
    return f"hola mundo desde una ruta redireccionada {ip}"




if __name__ == '__main__':
    app.run(debug=True)