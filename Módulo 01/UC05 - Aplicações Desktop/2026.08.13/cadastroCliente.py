import customtkinter as ctk
from tkinter import messagebox

# def cadastrar():
#     # showinfo, showwarning, showerror
#     messagebox.showinfo("Sucesso", "Cliente cadastrado")

def cadastrar():
    # ask
    resposta = messagebox.askyesno("Confirmar", "Deseja cadastrar esse cliente?")
    if resposta:
        messagebox.showinfo("Sucesso", "Cliente cadastrado")
    else:
        messagebox.showwarning("Cancelado", "Cadastro cancelado")

app = ctk.CTk()
app.title("Cadastro")
app.geometry("500x400")
app._set_appearance_mode("system")
# temas: light, dark, system

# app.grid_columnconfigure(0,weight=0) # coluna 0 não cresce
# app.grid_columnconfigure(1,weight=1) # coluna 1 cresce ocupando expaço extra

titulo = ctk.CTkLabel(
    app,
    text="Cadastro de Clientes",
    font=("Arial", 25, "bold"),
    text_color="#d9d9d8"
)
titulo.grid(
    row=0,
    column=0,
    padx=20,
    pady=20,
    columnspan=3
)

# FRAME - DADOS PESSOAIS
dados_frame = ctk.CTkFrame(app, fg_color="#b1bbc8")
dados_frame.grid(row=1, column=0, columnspan=2, stick="ew", padx=20)

nome = ctk.CTkLabel(
    app,
    text="Nome",
    font=("Arial", 15, "bold"),
    text_color="#b1bbc8"
)
nome.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

nome_entry = ctk.CTkEntry(
    app,
    placeholder_text="Digite seu nome",
    width=300, # largura
    height=35, # altura
    corner_radius=10, # arredondamento da forma
    border_color="#9fa4c4", # cor da borda
    border_width=2, # espessura da borda
    text_color="#133337", # cor do texto do entry
    placeholder_text_color="#c3c2f7" # cor do texto do placeholder
)
nome_entry.grid(
    row=1,
    column=1,
    pady=20
)

email = ctk.CTkLabel(
    app,
    text="Email",
    font=("Arial", 15, "bold"),
    text_color="#b1bbc8"
)
email.grid(
    row=2,
    column=0
)

email_entry = ctk.CTkEntry(
    app,
    placeholder_text="Digite seu nome",
    width=300, # largura
    height=35, # altura
    corner_radius=10, # arredondamento da forma
    border_color="#9fa4c4", # cor da borda
    border_width=2, # espessura da borda
    text_color="#133337", # cor do texto do entry
    placeholder_text_color="#c3c2f7"
)
email_entry.grid(
    row=2,
    column=1,
    pady=5
)

telefone = ctk.CTkLabel(
    app,
    text="Telefone",
    font=("Arial", 15, "bold"),
    text_color="#b1bbc8"
)
telefone.grid(
    row=3,
    column=0
)

telefone_entry = ctk.CTkEntry(
    app,
    placeholder_text="Digite seu telefone",
    width=300, # largura
    height=35, # altura
    corner_radius=10, # arredondamento da forma
    border_color="#9fa4c4", # cor da borda
    border_width=2, # espessura da borda
    text_color="#133337", # cor do texto do entry
    placeholder_text_color="#c3c2f7"
)
telefone_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=20
)

botao_cadastrar = ctk.CTkButton(
    app,
    text="Cadastrar",
    fg_color="#293447",
    hover_color="#052349",
    text_color="#d9d9d8",
    command=cadastrar
)
botao_cadastrar.grid(
    row=4,
    column=1,
    pady=20
)

app.mainloop()