

def recursos2():
    lista = [
        {
            "name" : "Luis",
            "age" : 30
        },
        {
            "name" : "nico",
            "age" : 26

        }
    ]
    return lista

def serializacion(lista): 
    import json 
    with open("data.json","w") as file : 
        json.dump(lista,file,indent=4)
        print("archivo json esrito con exito ... ")

def deserilizacion():
    import json 
    with open("data.json","r") as file : 
        data = json.load(file)
    #print(data)
    return data 
