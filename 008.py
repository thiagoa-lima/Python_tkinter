from tkinter import *

janela = Tk()
janela.title("TÍTULO")
janela.geometry("500x500")

# Posição do texto. Tipos de anchor: N, S, L, W, NE, SE, NW, SW, CENTER (Pontos Cardeais)
label_01 = Label(
    janela,
    text="123456789",
    font="Arial 20",
    bd=1,
    relief="solid",
    width=25,
    height=4,
    anchor=E,
)
label_01.pack()


label_01.pack()

janela.mainloop()
