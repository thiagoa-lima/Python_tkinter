from tkinter import *

menu_inicial =Tk()
menu_inicial.title("MENU INICIAL")

# Tipos de relif = flat, solid, raised, sunken, ridge, groove
border = 2
label_01 = Label(
    menu_inicial,
    text="flat",
    font="Arial 20 bold",
    bd=border,
    relief="flat",
)
label_01.pack()

label_01 = Label(
    menu_inicial,
    text="solid",
    font="Arial 20 bold",
    bd=border,
    relief="solid",
)
label_01.pack()

label_01 = Label(
    menu_inicial,
    text="raised",
    font="Arial 20 bold",
    bd=border,
    relief="raised",
)
label_01.pack()

label_01 = Label(
    menu_inicial,
    text="sunken",
    font="Arial 20 bold",
    bd=border,
    relief="sunken",
)
label_01.pack()

label_01 = Label(
    menu_inicial,
    text="groove",
    font="Arial 20 bold",
    bd=border,
    relief="groove",
)
label_01.pack()

menu_inicial.mainloop()
