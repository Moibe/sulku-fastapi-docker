import time
import avaimet

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

def authorize(userfile, work):

    print(f"Task received : {work}, type: {type(work)} ...")

    #Genera conexión inicial.
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)
    #Obtiene los tokens que hay en esa caja.
    tokens = avaimet.obtenTokens(sftpListo, caja)
    
    #True si autoriza o false si no autoriza.
    result = avaimet.autoriza(tokens, work)
    
    #Cierra la conexión.  
    avaimet.cierraConexion(sshListo, sftpListo)

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
