from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Meu menu")

label_01 = Label(
    menu_inicial,
    text="Label 01",
    font="Arial 20",
    bg="red",
    width=20,
    height=10
)
label_01.pack()

label_02 = Label(
    menu_inicial,
    text="Label 01",
    font="Arial 20",
    bg="green",
    width=20,
    height=5
)
label_02.pack()

menu_inicial.mainloop()
