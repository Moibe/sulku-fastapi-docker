import gradio as gr


def greet(name):
    #tokens = bafta()
    
    return "Tervetuloa " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

iface.launch()