import customtkinter as ctk

# criando uma janela (que vai ser uma variável)
app = ctk.CTk()
# o app vai receber a janela que é o ctk
# o .CTk é regra de uso, ele é uma classe criada pela comunidade para usar da melhor forma, sendo obrigatório para criar o molde
app.title("Login")
app.geometry("400x350") # largura e altura em pixel da tela que vai ser aberta

# título
titulo = ctk.CTkLabel(app, text="hello word!", font=("Arial", 24, "bold"))
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
subtitulo = ctk.CTkLabel(app, text="ciência da computação...")
subtitulo.pack(pady=(10, 20))
# esses valores é tipo, em cima vai espaçar 30 pixels e em baixo vai espaçar 50 pixels

# campo do usuário
entrada_user = ctk.CTkEntry(app, placeholder_text="semestre atual")
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

# botão do login
botao_login = ctk.CTkButton(app, text="Entrar")
botao_login.pack(pady=(10, 10))

app.mainloop() # manter a janela aberta