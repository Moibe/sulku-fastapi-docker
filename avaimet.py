import os
import time
import paramiko
import nycklar.nodes as nodes


def do():

  #Carga la firma digital para saber que confío en mi servidor de OpalStack.
  ssh = paramiko.SSHClient()
  ssh.load_host_keys("nycklar/itrst")

  #Ahora obtendremos nuestra secret key para poder entrar a ese servidor.
  # Obtiene la ruta del directorio actual
  project_dir = os.getcwd()
  print("Esto es projectdir: ", project_dir)
  path_completo = os.path.join(project_dir, "nycklar")

  print("Éste es el path_completo: ", path_completo)
  
  # Crea la ruta completa al archivo `go`
  key_filename = os.path.join(path_completo, "go")

  #Imprimo el path del id_rsa
  print("Esto es key_filename: ", key_filename)

  #Conexión hacia el servidor con tus credenciales.
  #Al tener una key no requieres el password.
  ssh.connect(nodes.realm, username=nodes.master, key_filename=key_filename)
  print(ssh)
  time.sleep(3)
  #Una vez que tenemos la conexión ssh, creamos un sftp (SSH File Transfer Protocol)
  sftp = ssh.open_sftp()
  print(sftp)
  time.sleep(3)
  

  # Ruta del archivo remoto
  archivo_remoto = nodes.avaimentekijä
  #archivo_remoto = "/home/moibe/apps/holocards/sulkusers/vallecanales.txt"
  print("Éste es el archivo remoto: ", archivo_remoto)
  time.sleep(5)

  with sftp.open(archivo_remoto, 'rb') as archivo:
    # Leer el contenido del archivo como bytes
    contenido_bytes = archivo.read()

    # Decodificar los bytes a Unicode usando la codificación UTF-8
    contenido_unicode = contenido_bytes.decode('utf-8')

    # Agregar el texto "- Revisado." al string
    contenido_final = int(contenido_unicode) - 1

    contenido_final = str(contenido_final)

    # Imprimir el contenido
    print(contenido_final)

    # Abrir el archivo remoto en modo escritura
  with sftp.open(archivo_remoto, 'w') as archivo:
    # Escribir el contenido final en el archivo
    archivo.write(contenido_final)

  sftp.close()
  ssh.close()

  return contenido_final