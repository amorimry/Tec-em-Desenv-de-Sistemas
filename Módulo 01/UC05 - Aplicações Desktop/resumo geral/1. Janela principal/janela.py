import customtkinter as ctk

# FUNÇÕES (exemplos, sem funcionalidade)
def entrar():
    pass
def criar_conta():
    pass

# INÍCIO --------------------------------
app = ctk.CTk()
# o app vai receber a janela que é o ctk (customtkinter renomeado no começo do código)
# o .CTk é regra de uso (acessar a classe), já que o customtkinter é uma classe criada pela comunidade para se usar da melhor forma, sendo obrigatório para criar o molde acessando o CTk

app.title("Título da janela") # aqui fica o título da janela
app.geometry("1000x500") # o formato da string de geometria é sempre "largura x altura" em pixel (Width x Height)

# TÍTULO --------------------------------
titulo = ctk.CTkLabel(app, text="Netflix", font=("Arial", 20, "bold"))
titulo.pack()

# Label é usado para tudo que for texto
# app é a primeira coisa que digita pois é a variável que recebeu o customtkinter
# text é o texto que vai ser apresentado da Label
# font é os parâmetros de fonte

# variavel.pack() --> o .pack() serve justamente para o objeto aparecer na tela
# dentro do .pack() também é possivel passar parâmetros que mexam com a forma de como vai ser mostrado na tela o que está sendo feito
    # Tipos de parâmentro para o pack:
        # 

# SUBTÍTULO --------------------------------
subtitulo = ctk.CTkLabel(app, text="Olá, entre na sua conta ou crie uma nova se caso não tiver.", font=("Arial", 15, "italic"))
subtitulo.pack()

# CAMPO DE DIGITAÇÃO --------------------------------
entrada_user = ctk.CTkEntry(app, placeholder_text="Digite o seu user...")
entrada_user.pack()

entrada_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha...")
entrada_senha.pack()

# o Entry é tipo um input
# placeholder_text é para poder colocar algo dentro do campo de digitação do Entry

# BOTÃO --------------------------------
login_botao = ctk.CTkButton(app, text="Entrar", cursor="hand2", command=entrar)
login_botao.pack()

criar_conta_botao = ctk.CTkButton(app, text="Criar conta", cursor="hand2", command=criar_conta)
criar_conta_botao.pack()

# o Button serve para criar botões
# command é para poder receber a ação (função) que, quando for clicado, o botão deve fazer
# cursos é para mudar o desenho do mouse quando ele passar por cima

# FIM --------------------------------
app.mainloop()
# manter a janela aberta
# ficar sempre no final do código