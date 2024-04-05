import gradio as gr
import avaimet

def authenticate(username, password):
    usuarios = [("usuario1", "contraseña1"), ("usuario2", "contraseña2")]
    for u, p in usuarios:
        if username == u and password == p:
            return True
    return False

def greet(user):
    
    tokens = avaimet.do()
    
    return "User: " + user + tokens + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

#iface.launch()
iface.launch(auth=authenticate)