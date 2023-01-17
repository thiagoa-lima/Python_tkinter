from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Meu menu")
menu_inicial.geometry("500x300")

# cores e tipo de letra
label_01 = Label(
    menu_inicial,
    text="Label 01",
    bg="#ff4d4d",
    fg="red",
    font="Arial"
)
label_01.pack()

label_02 = Label(
    text="Label 02",
    font="Verdana 50 bold italic",
    fg="#aaaaaa"
)
label_02.pack()
menu_inicial.mainloop()
