import customtkinter as ctk

# criando uma janela (que vai ser uma variável)
app = ctk.CTk()
# o app vai receber a janela que é o ctk
# o .CTk é regra de uso, ele é uma classe criada pela comunidade para usar da melhor forma, sendo obrigatório para criar o molde
app.title("Login")
app.geometry("400x350") # largura e altura em pixel da tela que vai ser aberta

# título
titulo = ctk.CTkLabel(app, text="hello word!")
# label é um texto que aparece na janela
# app é onde a label vai aparecer
# text é o texto que vai aparecer na label
titulo.pack()
# variavel.pack() serve para o objeto aparecer na tela


app.mainloop() # manter a janela aberta