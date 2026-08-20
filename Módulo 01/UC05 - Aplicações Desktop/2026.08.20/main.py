import customtkinter as ctk
from tkinter import ttk, messagebox
import database

# FUNÇÕES ======================
def adicionar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome.strip() == "" or telefone.strip() == "" or email.strip() =="":
        return messagebox.showwarning("Atenção","Os campos não podem estar em branco!")

    database.adicionar_contato(nome, telefone, email)

    entry_nome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")

    atualizar_tabela()

def atualizar_tabela():
    tabela.delete(*tabela.get_children())

    contatos = database.carregar_contatos()

    for contato in contatos:
        tabela.insert("", "end", values=(contato["nome"], contato["telefone"], contato["email"]))

def excluir():
    selecionado = tabela.selection()

    if not selecionado:
        return messagebox.showwarning("Atenção!", "Selecione um contato para excluir.")

    indice = tabela.index(selecionado[0])

    confirmar = messagebox.askyesno("Confirmar exclusão", "Tem certeza?")
    if confirmar:
        contatos = database.carregar_contatos()
        contatos.pop(indice)

        database.salvar_contatos(contatos)
        atualizar_tabela()

def abrir_popup_editar():
    selecionado = tabela.selection()

    if not selecionado:
        return messagebox.showwarning("Atenção!", "Selecione um contato para editar.")
    
    indice = tabela.index(selecionado[0])
    
    contatos = database.carregar_contatos()
    contato_atual = contatos[indice]
    
    # janela pop-up
    popup = ctk.CTkToplevel(janela)
    popup.title("Editar Contato")
    popup.geometry("350x300")
    popup.grab_set()
    
    ctk.CTkLabel(popup, text="Nome:").pack(anchor="w", padx=20, pady=(20, 0))
    entry_nome_popup = ctk.CTkEntry(popup)
    entry_nome_popup.pack(fill="x", padx=20)
    entry_nome_popup.insert(0, contato_atual["nome"])
 
    ctk.CTkLabel(popup, text="Telefone:").pack(anchor="w", padx=20, pady=(10, 0))
    entry_telefone_popup = ctk.CTkEntry(popup)
    entry_telefone_popup.pack(fill="x", padx=20)
    entry_telefone_popup.insert(0, contato_atual["telefone"])
 
    ctk.CTkLabel(popup, text="Email:").pack(anchor="w", padx=20, pady=(10, 0))
    entry_email_popup = ctk.CTkEntry(popup)
    entry_email_popup.pack(fill="x", padx=20)
    entry_email_popup.insert(0, contato_atual["email"])

    def salvar_edicao():
        novo_nome = entry_nome_popup.get()
        novo_telefone = entry_telefone_popup.get()
        novo_email = entry_email_popup.get()

        database.atualizar_contato(indice, novo_nome, novo_telefone, novo_email)
        atualizar_tabela()
        popup.destroy()
        
    botao_salvar = ctk.CTkButton(popup, text="Salvar", command=salvar_edicao)
    botao_salvar.pack(pady=20)

# Configurações da janela principal ======================
janela = ctk.CTk()
janela.title('Cadastro de clientes')
janela.geometry('600x680')


# TÍTULO ======================
titulo = ctk.CTkLabel(janela,text='Cadastro',font=('Arial', 28, 'bold'))
titulo.pack()

# CAMPOS DE ENTRADA (Nome,Telefone,Email) ======================
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


# TREEVIEW (lista de contatos) ======================
colunas = ("Nome", "Telefone", "Email")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

tabela.heading("Nome", text="Nome")
tabela.heading("Telefone", text="Telefone")
tabela.heading("Email", text="Email")

tabela.pack(fill="both", padx=20, pady=10)


# BOTÕES ======================
frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
frame_botoes.pack(padx=20, pady=(0, 20))

botao_adicionar = ctk.CTkButton(frame_botoes, text="Adicionar", command=adicionar)
botao_adicionar.pack(padx=5, side="left")

botao_editar = ctk.CTkButton(frame_botoes, text="Editar", command=abrir_popup_editar)
botao_editar.pack(padx=5, side="left")

botao_excluir = ctk.CTkButton(frame_botoes, text="Excluir", fg_color="#d9534f", hover_color="#c9302c", command=excluir)
botao_excluir.pack(padx=5, side="left")

atualizar_tabela()

janela.mainloop()