
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")

# Centralizar a janela no meio da tela
# Altura e largura do meu formulário
width = 500
height = 400

# Altura e largura da minha tela
screen_width = menu_inicial.winfo_screenwidth()
screen_height = menu_inicial.winfo_screenheight()

# Deifinição do eixo X e Y
x = int(screen_width/2 - width/2)
y = int(screen_height/2 - height/2)

# definir a geometria
menu_inicial.geometry(f"{width}x{height}+{x}+{y}")

menu_inicial.mainloop()
