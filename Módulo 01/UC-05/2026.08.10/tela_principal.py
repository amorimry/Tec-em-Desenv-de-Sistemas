import customtkinter as ctk

user_correto = "oie"
senha_correta = "123"

# criando uma janela (que vai ser uma variável)
app = ctk.CTk()
# o app vai receber a janela que é o ctk
# o .CTk é regra de uso, ele é uma classe criada pela comunidade para usar da melhor forma, sendo obrigatório para criar o molde
app.title("Login")
app.geometry("400x350") # largura e altura em pixel da tela que vai ser aberta

# título
titulo = ctk.CTkLabel(app, text="Bem-vindo!", font=("Arial", 24, "bold"))
# label é um texto que aparece na janela
# app é onde a label vai aparecer
# text é o texto que vai aparecer na label
# na fonte foi três parâmetros
titulo.pack(pady=(50,10))
# variavel.pack() serve para o objeto aparecer na tela
# no pack da tbm para passar parâmetros
    # pady é o espaçamento, em pixel, o primeiro valor é o eixo x e o segundo é o eixo y
    # mas oq foi anotado ai é um par de eixo x (eu acho)

# subtítulo (uma label abaixo do título)
subtitulo = ctk.CTkLabel(app, text="Faça seu login")
subtitulo.pack(pady=(10, 2))
# esses valores é tipo, em cima vai espaçar 30 pixels e em baixo vai espaçar 50 pixels

# campo do usuário
entrada_user = ctk.CTkEntry(app, placeholder_text="user")
# esse entry é o input
# o app é onde vai abrir oq eu to fazendo
# o placeholder_text é para colocar algo dentro do campo que o usuário está digitando
entrada_user.pack(pady=(10, 10))

# campo de senha
entrada_senha = ctk.CTkEntry(app, placeholder_text="senha")
# esse entry é o input
# o app é onde vai abrir oq eu to fazendo
# o placeholder_text é para colocar algo dentro do campo que o usuário está digitando
entrada_senha.pack(pady=(10, 10))

# label para mostrar erro de senha
erro_senha = ctk.CTkLabel(app, text="", text_color="red")
erro_senha.pack(pady=(2, 2))

def abrir_tela_principal():
    app.destroy() # fecha a tela de login e abre a outra janela automaticamente
    janela_principal = ctk.CTk()
    janela_principal.title("Área principal") # é o título da página por completo, pois ainda n é uma label
    janela_principal.geometry("400x350")
    janela_principal.mainloop()

def fazer_login():
    user = entrada_user.get() # pega o texto que vai ser digitado lá em cima
    senha = entrada_senha.get() # pega a senha / o .get é o comando que armazena
    # verificação:
    if user == user_correto and senha == senha_correta:
        abrir_tela_principal()
    else:
        erro_senha.configure(text="User ou senha incorreto.")
        # o .configure é para fazer alteração no que já foi criado

# botão do login
botao_login = ctk.CTkButton(app, text="Entrar", command=fazer_login)
# o command= serve para receber funções
botao_login.pack(pady=(2, 10))

# texto para cadastro
texto_cadastro = ctk.CTkLabel(app, text="Cadastre-se", cursor="hand2")
# o cursor é um parâmetro, que é o mouse e vai se transformar em hand2 que seria a mãozinha que o mouse se transforma
texto_cadastro.pack()

app.mainloop() # manter a janela aberta