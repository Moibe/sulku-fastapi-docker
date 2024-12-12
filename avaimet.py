import os
import tools
import paramiko
import nycklar.nodes as nodes


#AVAIMET CONTIENE LAS FUNCIONES QUE INTERACTUAN CON EL SERVIDOR REMOTO.
def conecta():

  #Digital Signature.
  ssh = paramiko.SSHClient()
  ssh.load_host_keys("nycklar/itrst")

  #Future: Para usar ésto el método connnect necesitaría aceptar la pk como var string.
  #go = os.getenv("go")
  
  #llave = paramiko.RSAKey(data=base64.b64decode(nycklar.go.texto))
  #clientPrivateKey = paramiko.RSAKey.from_private_key(nycklar.go.texto)

  #Ahora obtendremos nuestra secret key para poder entrar a ese servidor.
  project_dir = os.getcwd()
  #Ruta de go.
  key_filename = os.path.join(project_dir, "nycklar", "go")  
  
  ssh.connect(nodes.realm, username=nodes.master, key_filename=key_filename)
  #ssh.connect(nodes.realm, username=nodes.master, pkey=llave)
  sftp = ssh.open_sftp()

  return ssh, sftp

def obtenDireccionArchivo(archivo):
  #Archivo puede ser data.py o flagsnovelty.py

  # Ruta del archivo remoto (también general para todo lo que vive en holocards).
  ruta_remota = nodes.users_data
  path_archivo = ruta_remota + archivo

  return path_archivo


def obtenContenidoArchivo(sftp, dir_data):
    try:     
      with sftp.open(dir_data, 'rb') as archivo:               
        contenido = archivo.read()
        texto = contenido.decode('utf-8')      
    except Exception as e:
        texto = f"Error al leer el archivo: {e}"
        print(texto)
        return texto    
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

  #print(tokens)
  #Standard cost.
  costo_tarea = 2

  #Aplica reglas de cobro de tokens.
  #Posteriormente las equivalencias de tareas y costos vendrán de una tabla aparte.
  #Por ahora se definen via éste IF: 
  if work == 'picswap':
    costo_tarea = 1
    print(f"Work: {work}, tokens cost: {costo_tarea}")
  else:
    print("The work specified doesn't exists.")
    return False

  #Ahora evaluaremos si se tiene el suficiente crédito como para ejecutar la tarea.
  if tokens >= costo_tarea:
    #print("Tarea autorizada...")
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
  return 

def modificaQuota(sftp, dir_quota, quota, costo_proceso):

  print("Éste es quota: ", quota)
  print("Éste es costo_proceso: ", costo_proceso)

  #Standard cost.
  #cuantos = 30

  #Aplica reglas de quotas dinámicas.
  # if work == 'picswap':
  #   cuantos = 1
  #   print(f"Work: {work}, tokens cost: {cuantos}")
  # else:
  #   print("The work specified doesn't exists.")

  # Agregar el texto "- Revisado." al string
  contenido_final = int(quota) - int(costo_proceso)
  contenido_final = str(contenido_final)

  # Imprimir el contenido
  print(contenido_final)

  #Actualiza el nuevo valor en el servidor en modo escritura.
  with sftp.open(dir_quota, 'w') as archivo:
    # Escribir el contenido final en el archivo
    archivo.write(contenido_final)

  contenido_final = int(contenido_final)
  return contenido_final

def cierraConexion(ssh, sftp ):

  sftp.close()
  ssh.close()