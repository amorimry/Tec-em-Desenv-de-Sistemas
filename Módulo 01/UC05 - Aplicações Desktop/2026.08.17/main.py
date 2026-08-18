import customtkinter as ctk
from tkinter import ttk, messagebox #ttk para fazer a tabela
import database


#==========================================
#Funções
#==========================================
def adicionar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    #validação de string vazia ou espaços em branco
    if nome.strip() == "" and telefone.strip() == "" and email.strip() =="":
        return messagebox.showwarning('Atenção',"Os campos não podem estar em branco!")

    #=== Adicionar dados no banco ===
    database.adicionar_contato(nome, telefone, email)


#==========================================
#Configurações da janela principal
#==========================================

janela = ctk.CTk()
janela.title('Cadastro de clientes')
janela.geometry('600x680')

#==========================================
#TITULO
#==========================================

titulo = ctk.CTkLabel(janela,text='Cadastro',font=('Arial', 28, 'bold'))
titulo.pack()


#==========================================
#CAMPOS DE ENTRADA(Nome,Telefone,Email)
#==========================================

# frame_formulario = ctk.CTkFrame(janela)
# frame_formulario.pack(padx=20, pady=20, fill='x')

# label_nome = ctk.CTkLabel(frame_formulario, text='Nome')
# label_nome.pack(padx=10, pady=(10, 0))
# entry_nome = ctk.CTkEntry(frame_formulario, placeholder_text='Digite o seu nome')
# entry_nome.pack(padx=10, pady=(0, 10))

# label_telefone = ctk.CTkLabel(frame_formulario, text='Telefone')
# label_telefone.pack(padx=10, pady=(10, 0))
# entry_telefone = ctk.CTkEntry(frame_formulario, placeholder_text='Digite o seu telefone')
# entry_telefone.pack(padx=10, pady=(0, 10))

# label_email = ctk.CTkLabel(frame_formulario, text='email')
# label_email.pack(padx=10, pady=(10, 0))
# entry_email = ctk.CTkEntry(frame_formulario, placeholder_text='Digite o seu Email')
# entry_email.pack(padx=10, pady=(0, 10))

#--------------------------------------------

frame_formulario = ctk.CTkFrame(janela)
frame_formulario.pack(padx=20, pady=20, fill="x")

# Configura as colunas para expandirem corretamente
frame_formulario.grid_columnconfigure(1, weight=1)

# --- Campo Nome
label_nome = ctk.CTkLabel(frame_formulario, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_nome = ctk.CTkEntry(frame_formulario, placeholder_text="Digite o seu nome")
entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# --- Campo Telefone
label_telefone = ctk.CTkLabel(frame_formulario, text="Telefone:")
label_telefone.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_telefone = ctk.CTkEntry(frame_formulario, placeholder_text="Digite o seu telefone")
entry_telefone.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- Campo Email
label_email = ctk.CTkLabel(frame_formulario, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_email = ctk.CTkEntry(frame_formulario, placeholder_text="Digite o seu Email")
entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="ew")


#==========================================
#TREEVIEW (lista de contatos)
#==========================================

colunas = ("Nome", "Telefone", "Email")
tabela = ttk.Treeview(janela, columns=colunas, show="headings") #cria o objeto tabela

tabela.heading("Nome", text="Nome") #heading é de cabeçalho
tabela.heading("Telefone", text="Telefone")
tabela.heading("Email", text="Email")

tabela.pack(fill="both", padx=20, pady=10)


#==========================================
#BOTÕES
#==========================================
frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
frame_botoes.pack(padx=20, pady=(0, 20))

botao_adicionar = ctk.CTkButton(frame_botoes, text="Adicionar", command=adicionar)
botao_adicionar.pack(padx=5, side="left")

botao_editar = ctk.CTkButton(frame_botoes, text="Editar")
botao_editar.pack(padx=5, side="left")

botao_excluir = ctk.CTkButton(frame_botoes, text="Excluir", fg_color="#d9534f", hover_color="#c9302c")
botao_excluir.pack(padx=5, side="left")


janela.mainloop()