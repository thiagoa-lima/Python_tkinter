
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("primeiro app")

# define o tamanho padrao da janela e se pode ser alterado o tamanho
menu_inicial.geometry("500x250+400+250")
menu_inicial.resizable(True, True)
menu_inicial.iconbitmap("imagens/free.jpg")

# define a altura máxima e mínima da janela
menu_inicial.minsize(500, 250)
menu_inicial.maxsize(700, 400)


# a janela inicia maximizada. Se quiser iniciar minimizaca é só escrever "iconic"
#menu_inicial.state("zoomed")

menu_inicial.mainloop()
