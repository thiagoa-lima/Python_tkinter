
from tkinter import *

janela = Tk()

janela.title("MINHA JANELA")
janela.geometry("500x500")

# Justificação do texto: RIGHT, LEFT, CENTER
label_01 = Label(
    janela,
    text="frase de teste frase de teste frase de \nteste frase de teste frase de teste\nfrase de teste frase de teste",
    font="Arial 20",
    width=30,
    height=10,
    bd=1,
    relief="solid",
    justify=LEFT,
    anchor=E,
)
label_01.pack()


janela.mainloop()
