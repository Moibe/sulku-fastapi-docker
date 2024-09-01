import time
import avaimet

def getData():

    #Genera conexión inicial.       
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    data = avaimet.obtenData()
    
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
