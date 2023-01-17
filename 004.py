from tkinter import *

menu_inicial = Tk()

menu_inicial.title("Título")

label_01 = Label(menu_inicial, text="Esse é o label 01")
label_01.pack()

label_02 = Label(menu_inicial, text="Esse é o label 02")
label_02.pack()

btn_01 = Button(menu_inicial, text="Botão 01")
btn_01.pack()

menu_inicial.mainloop()
