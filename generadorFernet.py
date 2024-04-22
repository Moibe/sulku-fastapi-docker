from cryptography.fernet import Fernet

#Con este programa genero una llave de Fernet pero no tiene uso dentro de Sulku. 
#Podría usarse la clave que ya genere previamente.

# Generate a random 32-byte key
key = Fernet.generate_key()

# Print the key in base64-encoded format
print(key.decode('utf-8'))
