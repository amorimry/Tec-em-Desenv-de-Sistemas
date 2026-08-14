import tkinter as tk

class Cliente():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

c = Cliente("Pedro Henrique", "85 99999-9999")

janela = tk.Tk() #cria a janela
janela.title("AgendaFácil") #título da barra
janela.geometry("360x220") #largura x altura

#cada Label abaixo mostra um pedaço do objeto na tela
tk.Label(janela, text="Cliente Cadastrado",
         font=("Arial", 12)).pack(pady=(24, 4))

tk.Label(janela, text=c.nome,
         font=("Arial", 22)).pack()

tk.Label(janela, text=c.telefone,
         font=("Arial", 14)).pack(pady=6)

janela.mainloop() #mantem a janela aberta