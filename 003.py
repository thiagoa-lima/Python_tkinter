
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")

# dimensões da janela
largura = 500
altura = 400

# resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
print(largura_screen, altura_screen)


# posicão da janela
posicaoX = int(largura_screen/2 - largura/2)
posicaoY = int(altura_screen/2 - altura/2)

print(posicaoX, posicaoY)

# definir a geometria
menu_inicial.geometry(f"{largura}x{altura}+{posicaoX}+{posicaoY}")

menu_inicial.mainloop()
