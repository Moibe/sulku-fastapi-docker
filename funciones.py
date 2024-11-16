import ast
import time
import tools
import avaimet
import globales
import nycklar.nodes as nodes

#Aquí van las funciones principales, las que son llamadas directo por la API.
#Las que interactuan con el servidor están en el módulo avaimet.
#Y las herramientas adicionales están en tools.

def getData(aplicacion):
    
    sshListo, sftpListo = avaimet.conecta()
        
    #dir_data = avaimet.obtenDireccionArchivo() #Comenté éste pq me estaría ahorrando ésta función así:
    dir_data = nodes.users_data + aplicacion + globales.data

    print("Ésto es dir data...", dir_data)
    
    #Obtiene el json con los datos.
    data = avaimet.obtenContenidoArchivo(sftpListo, dir_data)    
    #Cierra la conexión.    
    avaimet.cierraConexion(sshListo, sftpListo)
    
    return data

def getTokens(userfile, env):
    #Genera conexión inicial.       
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile, env)
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

def debitTokens(userfile, work, env):

    print(f"Task received : {work}, type: {type(work)} ...")

    #Genera conexión inicial.
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile, env)
    #Obtiene los tokens que hay en esa caja.
    tokens = avaimet.obtenTokens(sftpListo, caja)
    #Aplica las reglas de ésta app para debitar lo correspondiente.
    resultado_debitado = avaimet.restaToken(sftpListo, caja, tokens, work)
    #Cierra la conexión.  
    avaimet.cierraConexion(sshListo, sftpListo)

    return resultado_debitado



def getUserNovelty(userfile, aplicacion):

    usuario = tools.decompileUser(userfile)
    
    #Genera conexión inicial (general para cualquier función.)  
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados las flags de novelty.
    #dir_data = avaimet.obtenDireccionArchivo(globales.novelty)
    dir_data = nodes.users_data + aplicacion + globales.novelty
    #Obtiene el json con los datos.
    data = avaimet.obtenContenidoArchivo(sftpListo, dir_data)
    
    # Convertir el string a una lista de tuplas utilizando ast.literal_eval()
    lista_tuplas = ast.literal_eval(data)
    tupla_encontrada = None  # Inicializamos una variable para almacenar la tupla encontrada

    avaimet.cierraConexion(sshListo, sftpListo)
    #Future, ¿se puede acaso que se cierre el contenido y que haga la conversión al mismo tiempo?    

    #Repasa todas las tuplas
    for tupla in lista_tuplas:
        if tupla[0] == usuario:
            tupla_encontrada = tupla
            break

    if tupla_encontrada:
        print("Usuario encontrado:", tupla_encontrada)
        novelty = tupla_encontrada[1]
        return novelty
    else:
        print("No se encontró ese usuario.")
        return "no user"