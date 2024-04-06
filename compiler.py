from cryptography.fernet import Fernet
import nycklar.nodes as nodes

def do(userfile):

    key = Fernet.generate_key()
    fernet = Fernet(key)

    string_original = "oldball182ls"
    string_encriptado = fernet.encrypt(string_original.encode("utf-8"))
    string_desencriptado = fernet.decrypt(userfile).decode("utf-8")

    print(f"String original: {string_original}")
    print(f"String encriptado: {string_encriptado}")
    print(f"String desencriptado: {string_desencriptado}")
