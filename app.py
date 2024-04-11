import time
import avaimet
import gradio as gr

def getAccess(userfile):

    #Genera conexión inicial.       
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)
    #Obtiene los tokens que hay en esa caja.
    tokens = avaimet.obtenTokens(sftpListo, caja)
    #Cierra la conexión.    
    avaimet.cierraConexion(sshListo, sftpListo)
    
    return tokens

def debitTokens(userfile, cuantos):

    #Genera conexión inicial.
    sshListo, sftpListo = avaimet.conecta()
    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)
    #Obtiene los tokens que hay en esa caja.
    tokens = avaimet.obtenTokens(sftpListo, caja)
    #Aplica las reglas de ésta app para debitar lo correspondiente.
    resultado_debitado = avaimet.restaToken(sftpListo, caja, tokens, cuantos)
    #Cierra la conexión.  
    avaimet.cierraConexion(sshListo, sftpListo)

    return resultado_debitado

#Interfaz Gráfica
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox()
            number_input = gr.Number()
            access_btn = gr.Button(value="Submit")
            debit_btn = gr.Button(value="Debit")
        with gr.Column():
            text_output = gr.Textbox()

    access_btn.click(fn=getAccess, inputs=text_input, outputs=text_output, api_name="getTokens")
    debit_btn.click(fn=debitTokens, inputs=[text_input, number_input], outputs=text_output, api_name="debitTokens")

demo.launch()