import os
import tools
import paramiko
#import compiler
import nycklar.nodes as nodes

#AVAIMET CONTIENE LAS FUNCIONES QUE INTERACTUAN CON EL SERVIDOR REMOTO.

def conecta():

  #Digital Signature.
  ssh = paramiko.SSHClient()
  ssh.load_host_keys("nycklar/itrst")

  #Ahora obtendremos nuestra secret key para poder entrar a ese servidor.
  project_dir = os.getcwd()
  
  #Ruta de go.
  key_filename = os.path.join(project_dir, "nycklar", "go")
  ssh.connect(nodes.realm, username=nodes.master, key_filename=key_filename)
  sftp = ssh.open_sftp()

  return ssh, sftp

def obtenDireccionArchivo(archivo):
  #Archivo puede ser data.py o flagsnovelty.py

  # Ruta del archivo remoto (también general para todo lo que vive en holocards).
  ruta_remota = nodes.users_data
  path_archivo = ruta_remota + archivo

  return path_archivo


def obtenContenidoArchivo(sftp, dir_data): 
    print("Estoy dentro de obtenContenido...")

    with sftp.open(dir_data, 'rb') as archivo:
      # Leer el contenido del archivo como bytes
      print("Pude entrar al archivo...")
      contenido = archivo.read()
      print("Imprimiendo contenido: ", contenido)
      print("El tipo de contenido obtenido es: ", type(contenido))

      #Decodificar pq viene codificado del server (codificado en bytes) no encriptado.      
      texto = contenido.decode('utf-8')
      
      return texto

def obtenCaja(userfile, env):

  #Codifica y descomprime el string para obtener un user.
  username = tools.decompileUser(userfile)

  # Ruta del archivo remoto
  ruta_remota = nodes.users_credits + env + "/"
  caja = ruta_remota + username + ".txt"
    
  return caja

def obtenTokens(sftp, caja): 
   
    with sftp.open(caja, 'rb') as archivo:
      # Leer el contenido del archivo como bytes
      contenido_bytes = archivo.read()
      # Decodificar los bytes a Unicode usando la codificación UTF-8
      tokens = contenido_bytes.decode('utf-8')

      tokens = int(tokens)

      return tokens
    
def autoriza(tokens, work):

  print(tokens)

  #Standard cost.
  costo_tarea = 2

  #Aplica reglas de cobro de tokens.
  #Posteriormente las equivalencias de tardeas y costos vendrán de una tabla aparte.
  #Por ahora se definen via éste IF: 
  if work == 'picswap':
    costo_tarea = 1
    print(f"Work: {work}, tokens cost: {costo_tarea}")
  else:
    print("The work specified doesn't exists.")
    return False

  #Ahora evaluaremos si se tiene el suficiente crédito como para ejecutar la tarea.
  if tokens >= costo_tarea:
    print("Tarea autorizada...")
    result = True
  else:
     print("Tarea no autorizada, no tienes suficientes tokens...")
     result = False
  
  return result
    
def restaToken(sftp, caja, tokens, work):

  #Standard cost.
  cuantos = 2

  #Aplica reglas de cobro de tokens.
  if work == 'picswap':
    cuantos = 1
    print(f"Work: {work}, tokens cost: {cuantos}")
  else:
    print("The work specified doesn't exists.")

  # Agregar el texto "- Revisado." al string
  contenido_final = int(tokens) - cuantos
  contenido_final = str(contenido_final)

  # Imprimir el contenido
  print(contenido_final)

  #Actualiza el nuevo valor en el servidor en modo escritura.
  with sftp.open(caja, 'w') as archivo:
    # Escribir el contenido final en el archivo
    archivo.write(contenido_final)

  contenido_final = int(contenido_final)
  return contenido_final

def cierraConexion(ssh, sftp ):

  sftp.close()
  ssh.close()