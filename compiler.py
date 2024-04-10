import time 
import nycklar.nodes as nodes
from cryptography.fernet import Fernet

def do(desencriptable):

    print("El tipo de desencriptable desde adentro es es del tipo: ", type(desencriptable))
    time.sleep(8)

    #key = Fernet.generate_key()
    key = nodes.key
    print("Esto es la KEY: ", key)
    time.sleep(1)
    fernet = Fernet(key)
    print("Esto es Fernet: ", fernet)
    
    string_desencriptado = fernet.decrypt(desencriptable).decode("utf-8")

    print(f"String desencriptado: {string_desencriptado}")
    time.sleep(5)

    return string_desencriptado