import customtkinter as ctk

# janela
app = ctk.CTk()
app.title("Cadastro")
app.geometry("500x400")

# título
titulo = ctk.CTkLabel(
    app,
    text="Cadastro de Clientes",
    font=("Serif", 20, "bold")
)
titulo.grid(
    row=0,
    column=0,
    padx=10,
    columnspan=2
)
# o grid são linhas e colunas imaginarias que vão aparecendo conforme vai sendo colocando os geds
# row é linha e column é coluna

# cadastro
nome = ctk.CTkLabel(
    app,
    text="nome"
)
nome.grid(
    row=1,
    column=0,
    sticky="w", # w e n s / w = equerda, e = direita, n = cima, s = baixo
    padx=10
)

entry_nome = ctk.CTkEntry(
    app,
    placeholder_text="Digite seu nome"
)
entry_nome.grid(
    row=2,
    column=1
)

app.mainloop()