
import json 
import os 

lista=[]

def Serializacion(lista):

    file_name = "data.json"

    if os.path.exists(file_name) : 

        with open(file_name , "r") as File : 

            data =json.load(File)
            print(data)# todo es un dic 
            lista.append(data)
            
        
        with open(file_name , "w" ) as File : 
           
            json.dump(data,File,indent=4)
            
        
    else : 
       
        with open(file_name,"w") as File : 

            json.dump(lista,File,indent=4)
          