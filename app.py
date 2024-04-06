import gradio as gr
import avaimet

def authenticate(username, password):
    usuarios = [("usuario1", "contrasena1"), ("usuario2", "contrasena2")]
    for u, p in usuarios:
        if username == u and password == p:
            return True
    return False

def getAccess(userfile):
    
    tokens = avaimet.do(userfile)
    
    return tokens

iface = gr.Interface(fn=getAccess, inputs="text", outputs="text")

#iface.launch()
iface.launch(auth=authenticate)