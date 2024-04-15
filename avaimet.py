import os
import time
import paramiko
import compiler
import nycklar.nodes as nodes

def conecta():

  #Digital Signature.
  ssh = paramiko.SSHClient()
  ssh.load_host_keys("nycklar/itrst")

  #Ahora obtendremos nuestra secret key para poder entrar a ese servidor.
  project_dir = os.getcwd()
  key_filename = os.path.join(project_dir, "nycklar", "go")
   
  ssh.connect(nodes.realm, username=nodes.master, key_filename=key_filename)
  sftp = ssh.open_sftp()

  return ssh, sftp

def obtenCaja(userfile):

  print("Esto es userfile de obtenCaja: ", userfile)
  time.sleep(9)
  # Ruta del archivo remoto
  ruta_remota = nodes.avaimentekijä
  print("Encoding...")
  userfile_codificado = userfile.encode("utf-8")
  print(f"El userfile sin la b, se decodifica y queda: {userfile_codificado} y es del tipo {type(userfile_codificado)} ...")
  time.sleep(3)
    
  print("Estoy afuera, enviando al compiler.")
  username = compiler.do(userfile_codificado)
  print("Username es: ", username)
  caja = ruta_remota + username + ".txt"
  print("Éste es el archivo remoto: ", caja)
  
  return caja

def obtenTokens(sftp, caja): 
   
    with sftp.open(caja, 'rb') as archivo:
      # Leer el contenido del archivo como bytes
      contenido_bytes = archivo.read()
      # Decodificar los bytes a Unicode usando la codificación UTF-8
      tokens = contenido_bytes.decode('utf-8')

      print("Tokens son....: ", tokens)
      print("Y su type182 es: ", type(tokens))
      time.sleep(8)

      return tokens
    
def restaToken(sftp, caja, tokens, work):

  #Standard cost.
  cuantos = 2

  #Aplica reglas de cobro de tokens.
  if work == 'picswap':
    cuantos = 1
    print(f"Work: {work}, cuantos: {cuantos}")
    time.sleep(3)
  else:
    print("El trabajo no existe...")


  # Agregar el texto "- Revisado." al string
  contenido_final = int(tokens) - cuantos
  contenido_final = str(contenido_final)

  # Imprimir el contenido
  print(contenido_final)

  #Actualiza el nuevo valor en el servidor en modo escritura.
  with sftp.open(caja, 'w') as archivo:
    # Escribir el contenido final en el archivo
    archivo.write(contenido_final)

  return contenido_final

def cierraConexion(ssh, sftp ):

  sftp.close()
  ssh.close()
