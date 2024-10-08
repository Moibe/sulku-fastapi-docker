import ast
import tools
import avaimet
import globales

#Aquí van las funciones principales, las queson llamadas directo por la API.
#Las que interactuan con el servidor están en el módulo avaimet.
#Y las herramientas adicionales están en tools.

def getData():
    #Genera conexión inicial.       
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    #Future: Ese data.py después puede viri en un globales.
    dir_data = avaimet.obtenDireccionArchivo(globales.data)
    #Obtiene el json con los datos.
    data = avaimet.obtenContenidoArchivo(sftpListo, dir_data)    
    #Cierra la conexión.    
    avaimet.cierraConexion(sshListo, sftpListo)
    
    return data

def getTokens(userfile):
    #Genera conexión inicial.       
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)
    #Obtiene los tokens que hay en esa caja.
    tokens = avaimet.obtenTokens(sftpListo, caja)
    #Cierra la conexión.    
    avaimet.cierraConexion(sshListo, sftpListo)
    
    return tokens

def authorize(tokens, work):

    print(f"Task received : {work}, type: {type(work)} ...")

    ##Ésta sección se reutilizará si en lugar de pasar el parámetro token, se pasa el parámetro userfile.
    #Actualmente no lo pedimos porque es el developer el que pone la cantidad de tokens que el usuario tiene para...
    #...evitar otra vuelta al server, por mayor certeza o seguridad se puede hacer esa ida. 
    #En un futuro incluso se pueden hacer los dos tipos de autorización en dos endpoints distintos. O en un solo endpoint con...
    #...las dos opciones. 

    #Genera conexión inicial.
    #sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    #caja = avaimet.obtenCaja(userfile)
    #Obtiene los tokens que hay en esa caja.
    #tokens = avaimet.obtenTokens(sftpListo, caja)
    
    #True si autoriza o false si no autoriza.
    result = avaimet.autoriza(tokens, work)
    
    #Cierra la conexión.  
    #avaimet.cierraConexion(sshListo, sftpListo)

    return result

def debitTokens(userfile, work):

    print(f"Task received : {work}, type: {type(work)} ...")

    #Genera conexión inicial.
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)
    #Obtiene los tokens que hay en esa caja.
    tokens = avaimet.obtenTokens(sftpListo, caja)
    #Aplica las reglas de ésta app para debitar lo correspondiente.
    resultado_debitado = avaimet.restaToken(sftpListo, caja, tokens, work)
    #Cierra la conexión.  
    avaimet.cierraConexion(sshListo, sftpListo)

    return resultado_debitado



def getUserFlag(userfile):

    usuario = tools.decompileUser(userfile)
    
    #Genera conexión inicial (general para cualquier función.)  
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados las flags.
    #Future: Que flags.py venga de globales.
    dir_data = avaimet.obtenDireccionArchivo(globales.flags)
    #Obtiene el json con los datos.
    data = avaimet.obtenContenidoArchivo(sftpListo, dir_data)
    
    # Convertir el string a una lista de tuplas utilizando ast.literal_eval()
    lista_tuplas = ast.literal_eval(data)
    tupla_encontrada = None  # Inicializamos una variable para almacenar la tupla encontrada

    avaimet.cierraConexion(sshListo, sftpListo)
    #Future, ¿se puede acaso que se cierre el contenido y que haga la conversión al mismo tiempo?    

    for tupla in lista_tuplas:
        if tupla[0] == usuario:
            tupla_encontrada = tupla
            break

    if tupla_encontrada:
        print("La tupla encontrada es:", tupla_encontrada)
        flag = tupla_encontrada[1]
        return flag
    else:
        print("No se encontró ninguna tupla con el texto especificado.")
        return "no user"