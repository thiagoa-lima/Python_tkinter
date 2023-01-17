from tkinter import *

menu_inicial = Tk()

menu_inicial.title("Título")
# menu_inicial["bg"] = "gray"
menu_inicial.geometry("500x300+400+250")


# botão
def btn_Click(mensagem):
    print(mensagem)


btn_01 = Button(
    menu_inicial,
    text="Exceutar",
    command=lambda: btn_Click("Nova mensagem")
)
btn_01.pack()

btn_02 = Button(
    menu_inicial,
    text="Clicar",
    command=lambda: print("OK")
)
btn_02.pack()

menu_inicial.mainloop()
