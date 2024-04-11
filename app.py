import time
import avaimet
import gradio as gr

def getAccess(userfile):
        
    sshListo, sftpListo = avaimet.conecta()

    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)

    tokens = avaimet.obtenTokens(sftpListo, caja)

    resultado_final = avaimet.aplicaReglas(sftpListo, caja, tokens)

    avaimet.cierraConexion(sshListo, sftpListo)
    
    return resultado_final

def ask(sulkukey):

    print("Hola mundo")

    return 1

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox()
            access_btn = gr.Button(value="Submit")
            debit_btn = gr.Button(value="Debit")
        with gr.Column():
            text_output = gr.Textbox()

    access_btn.click(fn=getAccess, inputs=text_input, outputs=text_output, api_name="getTokens")
    debit_btn.click(fn=ask, inputs=text_input, outputs=text_output, api_name="print")

demo.launch()