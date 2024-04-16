import time 
import nycklar.nodes as nodes
from cryptography.fernet import Fernet

def do(desencriptable):

    #key = Fernet.generate_key()
    key = nodes.key
    fernet = Fernet(key)
    string_desencriptado = fernet.decrypt(desencriptable).decode("utf-8")

    return string_desencriptado