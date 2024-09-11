import compiler

#Tools son herramientas adicionales que usan todos.

def decompileUser(userfile):

    print("Encoding...")
    #Con ésta acción de encode lo que está haciendo es agregarle la 'b, o sea lo vuelve al tipo q necesitamos pero no modifica los datos.
    userfile_codificado = userfile.encode("utf-8")

    #Ahora si ésta parte va a convertir el string largo en el verdadero nombre de usuario.    
    print("Sending to compiler.")
    username = compiler.do(userfile_codificado)
    print("Username is: ", username)
    
    return username
