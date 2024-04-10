import time 
import nycklar.nodes as nodes
from cryptography.fernet import Fernet

key = nodes.key
print("Esto es la KEY: ", key)
time.sleep(1)
fernet = Fernet(key)
print("Esto es Fernet: ", fernet)

string_original = "revgenlabs"
string_encriptado = fernet.encrypt(string_original.encode("utf-8"))
string_desencriptado = fernet.decrypt(string_encriptado).decode("utf-8")

print("Guarda esto: ", string_encriptado)
print("Viene de aquí: ", string_desencriptado)