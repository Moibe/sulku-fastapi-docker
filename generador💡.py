import time 
import nycklar.nodes as nodes
from cryptography.fernet import Fernet

key = nodes.key
fernet = Fernet(key)

string_original = "revgenlabs"
string_encriptado = fernet.encrypt(string_original.encode("utf-8"))
string_desencriptado = fernet.decrypt(string_encriptado).decode("utf-8")